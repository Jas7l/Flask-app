from flask import Blueprint
from flask_login import login_required
from ..service.user_manager import UserManager


user_bp = Blueprint('user', __name__, url_prefix="/api/user")


@user_bp.route("/login", methods=["POST"])
def login():
    return UserManager.login()


@user_bp.route("/logout", methods=["POST"])
@login_required
def logout():
    return UserManager.logout()


@user_bp.route("/info", methods=["GET"])
@login_required
def user_info():
    return UserManager.user_info()
