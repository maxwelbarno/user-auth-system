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
