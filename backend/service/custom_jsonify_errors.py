from flask import jsonify
from http import HTTPStatus


class JsonifyErrors:
    @staticmethod
    def login_is_busy():
        return jsonify({
            "error": "error|warning|notice",
            "code": HTTPStatus.BAD_REQUEST,
            "message": "User with this login already exist",
            "data": {}})

    @staticmethod
    def passwords_not_match():
        return jsonify({
            "error": "error|warning|notice",
            "code": HTTPStatus.BAD_REQUEST,
            "message": "Passwords don't match",
            "data": {}})

    @staticmethod
    def login_fields():
        return jsonify({
            "error": "error|warning|notice",
            "code": HTTPStatus.BAD_REQUEST,
            "message": "Missing one of fields",
            "data": {
                "login": "Your login",
                "password": "Your password",
                "ad_password": "Repeat password"
            }})

    @staticmethod
    def inactive_user():
        return jsonify({
                    "error": "error|warning|notice",
                    "code": HTTPStatus.FORBIDDEN,
                    "message": "User is inacrive",
                    "data": {}})

    @staticmethod
    def unauthorized_loggout():
        return jsonify({
            "error": "error|warning|notice",
            "code": HTTPStatus.UNAUTHORIZED,
            "message": "Unauthorized user can't logout",
            "data": {}})

    @staticmethod
    def user_not_exist():
        return jsonify({
                    "error": "error|warning|notice",
                    "code": HTTPStatus.NOT_FOUND,
                    "message": "User with this id doesn't exist",
                    "data": {}})
