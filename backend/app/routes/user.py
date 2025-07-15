from flask import Blueprints, jsonify
from flask_login import login_required

user_bp = Blueprints('user', __name__, url_prefix="/api/user")


@user_bp.route("/login", methods=["POST"])
def login():
    return


@user_bp.route("/logout", methods=["POST"])
def logout():
    return


@user_bp.route("/info", methods=["GET"])
@login_required
def user_info():
    return
