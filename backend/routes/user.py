from flask import Blueprint, request, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from http import HTTPStatus
from ..models.user import User
from ..schemas.user import PrintUser
from ..database import SessionLocal
import bcrypt

user_bp = Blueprint('user', __name__, url_prefix="/api/user")


@user_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    login_input = data["login"]
    password_input = data["password"]

    with SessionLocal as db:
        user = db.query(User).filter(User.login == login_input).first()

        if not user or not bcrypt.checkpw(password_input.encode(), user.password):
            return jsonify({"message": "Missing login or password"}), HTTPStatus.BAD_REQUEST

        login_user(user)
        return jsonify({"message": "Login successful"}), HTTPStatus.OK


@user_bp.route("/logout", methods=["POST"])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logged out"}), HTTPStatus.OK


@user_bp.route("/info", methods=["GET"])
@login_required
def user_info():
    user_out = PrintUser.from_orm(current_user)
    return jsonify(user_out.dict()), HTTPStatus.OK
