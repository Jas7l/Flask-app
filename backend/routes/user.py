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


@user_bp.route("/register", methods=["POST"])
def register():
    return UserManager.register()


@user_bp.route("/info", methods=["GET"])
@login_required
def user_info():
    return UserManager.user_info()


@user_bp.route("/update/<int:orbis_id>", methods=["PATCH"])
def update_user(orbis_id):
    return UserManager.update_user(orbis_id)


@user_bp.route("/delete/<int:orbis_id>", methods=["DELETE"])
def set_user_inactive(orbis_id):
    return UserManager.set_user_inactive(orbis_id)


@user_bp.route("/email", methods=["POST"])
@login_required
def send_email():
    return UserManager.send_email()
