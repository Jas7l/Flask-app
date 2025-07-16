from flask import request, jsonify
from flask_login import login_user, logout_user, current_user
from http import HTTPStatus
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
        user_out = PrintUser.from_orm(current_user)
        return jsonify(user_out.dict()), HTTPStatus.OK
