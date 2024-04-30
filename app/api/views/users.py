from flask import Blueprint, request, jsonify
from ..models.user import User
from utils.validations import check_for_blanks, validate_key_value_pairs
from utils.responses import response

users_blueprint = Blueprint("blueprint", __name__)


class Registration:
    """User registration endpoint"""

    @users_blueprint.route("/register", methods=["POST"])
    # Decorators are used to associate URL routes with the view functions defined within the blueprint
    def registerUser(self):

        key_value_errors = validate_key_value_pairs(request)
        if key_value_errors:
            return response(
                "{} key is missing".format(", ".join(key_value_errors)), 400
            )

        data = request.get_json()
        blanks = check_for_blanks(data)

        if blanks:
            return response("{} cannot be blank!".format(", ".join(blanks)), 400)

        username = data.get("username")
        password = data.get("password")

        user = User()
        search = user.find_by_username(username)
        if search:
            return response("username {} is already registered!".format(search[1]), 400)

        user.create(username, password)
        return response("user registered successfully!", 201)


class Login:
    """User login endpoint"""

    @users_blueprint.route("/login", methods=["POST"])
    def userlogin(self):
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        user = User()

        login = user.login(username, password)

        return (
            response("login successful", 200)
            if login
            else response("authentication error!", 401)
        )
