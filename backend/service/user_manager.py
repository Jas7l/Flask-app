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

            if not user or not bcrypt.checkpw(password_input.encode(), user.password):
                return jsonify({"message": "Missing login or password"}), HTTPStatus.BAD_REQUEST

            login_user(user)
            user.active = True
            db.commit()
            db.refresh(user)
            return jsonify({"message": "Login successful"}), HTTPStatus.OK

    @staticmethod
    def logout():
        with get_db() as db:
            current_user.active = False
            db.add(current_user)
            db.commit()
            db.refresh(current_user)
        logout_user()
        return jsonify({"message": "Logged out"}), HTTPStatus.OK

    @staticmethod
    def user_info():
        login = current_user.login
        result = UserManager.user_info_by_login(login)
        if not result:
            return jsonify({"message": "User not found"}), HTTPStatus.NOT_FOUND
        return jsonify(result), HTTPStatus.OK

    @staticmethod
    def user_info_by_login(login_input: str):
        with get_db() as db:
            user_table = Table('users', MetaData(), autoload_with=db.bind)

            columns = [col for col in user_table.columns if col.name != "password"]
            req = select(*columns).where(user_table.c.login == login_input)
            result = db.execute(req).first()

            if not result:
                return None

            return dict(zip([col.name for col in columns], result))
