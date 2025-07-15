from flask import Blueprints, request ,jsonify
from flask_login import login_user, logout_user, login_required, current_user
from ..models.user import User
from ..database import  SessionLocal
import bcrypt

user_bp = Blueprints('user', __name__, url_prefix="/api/user")


@user_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    login_input = data["login"]
    password_input = data["password"]


    with SessionLocal as db:
        user = db.query(User).filter(User.login == login_input).first()

        if not user or not  bcrypt.checkpw(password_input.encode(), user.password):
            return jsonify({"message": "Missing login or password"}), 400
    return


@user_bp.route("/logout", methods=["POST"])
def logout():
    return


@user_bp.route("/info", methods=["GET"])
@login_required
def user_info():
    return
