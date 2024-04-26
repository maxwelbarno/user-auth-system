from flask import Blueprint, request, jsonify
from ..models.user import User

user = Blueprint("user", __name__)


class Registration:
    """User registration endpoint"""

    @user.route("/register", methods=["POST"])
    def registerUser():
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        user = User()
        data = {"data": user.create(username, password)}

        return jsonify(data), 201


class Login:
    """User login endpoint"""

    @user.route("/login", methods=["POST"])
    def userlogin():
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        user = User()

        login = user.login(username, password)

        if login:
            return jsonify({"message": "login success"}), 200
        else:
            return jsonify({"message": "login failed"}), 401
