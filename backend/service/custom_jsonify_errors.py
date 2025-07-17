from flask import jsonify
from http import HTTPStatus


class JsonifyErrors:
    @staticmethod
    def login_is_busy():
        return jsonify({
            "error": "error|warning|notice",
            "code": HTTPStatus.BAD_REQUEST,
            "message": "User with this login already exist",
            "data": {}}), HTTPStatus.BAD_REQUEST

    @staticmethod
    def passwords_not_match():
        return jsonify({
            "error": "error|warning|notice",
            "code": HTTPStatus.BAD_REQUEST,
            "message": "Passwords don't match",
            "data": {}}), HTTPStatus.BAD_REQUEST

    @staticmethod
    def login_fields():
        return jsonify({
            "error": "error|warning|notice",
            "code": HTTPStatus.BAD_REQUEST,
            "message": "Missing one of fields",
            "data": {
                "login": "required",
                "password": "required",
                "ad_password": "required"
            }}), HTTPStatus.BAD_REQUEST

    @staticmethod
    def inactive_user():
        return jsonify({
                    "error": "error|warning|notice",
                    "code": HTTPStatus.FORBIDDEN,
                    "message": "User is inacrive",
                    "data": {
                        "active": "False"
                    }}), HTTPStatus.FORBIDDEN

    @staticmethod
    def unauthorized_logout():
        return jsonify({
            "error": "error|warning|notice",
            "code": HTTPStatus.UNAUTHORIZED,
            "message": "Unauthorized user can't logout",
            "data": {}}), HTTPStatus.UNAUTHORIZED

    @staticmethod
    def user_not_exist():
        return jsonify({
                    "error": "error|warning|notice",
                    "code": HTTPStatus.NOT_FOUND,
                    "message": "User with this id doesn't exist",
                    "data": {}}), HTTPStatus.NOT_FOUND

    @staticmethod
    def invalid_user_info():
        return jsonify({
            "id": 1000,
            "fields": {}
        }), HTTPStatus.NOT_FOUND

    @staticmethod
    def missing_login_pas():
        return jsonify({
                    "error": "error|warning|notice",
                    "code": HTTPStatus.BAD_REQUEST,
                    "message": "Missing login or password",
                    "data": {
                        "login": "required",
                        "password": "required"
                    }}), HTTPStatus.BAD_REQUEST
