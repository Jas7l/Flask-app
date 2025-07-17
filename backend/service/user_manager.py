from flask import request, jsonify
from flask_login import login_user, logout_user, current_user
from http import HTTPStatus
from sqlalchemy import Table, MetaData, select
from ..models.user import User
from ..schemas.user import PrintUser
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
                return jsonify({"message": "User is inactive"}), HTTPStatus.FORBIDDEN

            if not user or not bcrypt.checkpw(password_input.encode(), user.password):
                return jsonify({"message": "Missing login or password"}), HTTPStatus.BAD_REQUEST

            login_user(user)
            return jsonify({"message": "Login successful"}), HTTPStatus.OK

    @staticmethod
    def logout():
        logout_user()
        return jsonify({"message": "Logged out"}), HTTPStatus.OK

    @staticmethod
    def user_info():
        input_id = int(current_user.orbis_id)
        result = UserManager.user_info_by_id(input_id)
        if not result:
            return jsonify({"message": "User not found"}), HTTPStatus.NOT_FOUND
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

            return dict(zip([col.name for col in columns], result))
