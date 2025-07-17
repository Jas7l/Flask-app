from flask import request, jsonify
from flask_login import login_user, logout_user, current_user
from http import HTTPStatus
from sqlalchemy import Table, MetaData, select
from ..models.user import User
from .custom_jsonify_errors import JsonifyErrors
from ..database import get_db
import bcrypt


class UserManager:
    @staticmethod
    def login():
        data = request.get_json()
        login_input = data["login"]
        password_input = data["password"]

        with get_db() as db:
            user = db.query(User).filter(User.login == login_input).first()

            if user.active is False:
                return JsonifyErrors.inactive_user()

            if not user or not bcrypt.checkpw(password_input.encode(), user.password):
                return JsonifyErrors.missing_login_pas()

            login_user(user)
            return jsonify({"message": "Login successful",
                           "code": HTTPStatus.OK}), HTTPStatus.OK

    @staticmethod
    def register():
        data = request.get_json()
        fields = data.get("fields", {})
        login_input = fields.get("login")
        password_input = fields.get("password")
        ad_password_input = fields.get("ad_password")

        if not login_input or not password_input or not ad_password_input:
            return JsonifyErrors.login_fields()

        if password_input != ad_password_input:
            return JsonifyErrors.passwords_not_match()

        with get_db() as db:
            if db.query(User).filter(User.login == login_input).first():
                return JsonifyErrors.login_is_busy()

            hashed_password = bcrypt.hashpw(password_input.encode("utf-8"), bcrypt.gensalt())

            new_user = User(
                login=login_input,
                password=hashed_password
            )

            db.add(new_user)
            db.commit()

            new_user_info = UserManager.user_info_by_id(new_user.orbis_id)

            if not new_user_info:
                return JsonifyErrors.user_not_exist()
            return jsonify(new_user_info), HTTPStatus.OK

    @staticmethod
    def logout():
        if not current_user.is_authenticated:
            return JsonifyErrors.unauthorized_logout()
        logout_user()
        return jsonify({
            "message": "Logged out",
            "code": HTTPStatus.OK}), HTTPStatus.OK

    @staticmethod
    def user_info():
        input_id = int(current_user.orbis_id)
        result = UserManager.user_info_by_id(input_id)
        if not result:
            return JsonifyErrors.invalid_user_info()
        return jsonify(result), HTTPStatus.OK

    @staticmethod
    def user_info_by_id(input_id: int):
        with get_db() as db:
            user_table = Table('users', MetaData(), autoload_with=db.bind)

            columns = [col for col in user_table.columns if col.name != "password"]
            req = select(*columns).where(user_table.c.orbis_id == input_id)
            result = db.execute(req).first()

            if not result:
                return None

            row_dict = dict(zip([col.name for col in columns], result))
            user_id = row_dict.pop("orbis_id")
            return {
                "id": user_id,
                "fields": row_dict
            }

    @staticmethod
    def update_user(input_id: int):
        data = request.get_json()
        fields = data.get("fields", {})

        with get_db() as db:
            user = db.query(User).get(input_id)
            if not user:
                return JsonifyErrors.user_not_exist()

            login = fields.get("login")
            if login is not None:
                if not isinstance(login, str):
                    return JsonifyErrors.incorrect_login()
                user.login = login

            password = fields.get("password")
            if password is not None:
                if not isinstance(password, str):
                    return JsonifyErrors.incorrect_password()
                user.password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

            active = fields.get("active")
            if active is not None:
                if not isinstance(active, bool):
                    return JsonifyErrors.incorrect_active()
                user.active = active

            db.add(user)
            db.commit()

            user_info = UserManager.user_info_by_id(user.orbis_id)

            if not user_info:
                return JsonifyErrors.invalid_user_info()
            return jsonify(user_info), HTTPStatus.OK

    @staticmethod
    def set_user_inactive(input_id: int):
        with get_db() as db:
            user = db.query(User).get(input_id)
            if not user:
                return JsonifyErrors.user_not_exist()

            user.active = False

            db.commit()
            return jsonify(True), HTTPStatus.OK
