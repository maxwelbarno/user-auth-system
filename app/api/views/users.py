import jwt
from flask import Blueprint, request, current_app
from ..models.user import User
from utils.validations import check_for_blanks, validate_key_value_pairs
from utils.responses import response, response_with_data
from utils.decorators import jwt_required

users_blueprint = Blueprint("blueprint", __name__)


@users_blueprint.route("/register", methods=["POST"])
# Decorators are used to associate URL routes with the view functions defined within the blueprint
def register_user():
    """User registration endpoint"""

    key_value_errors = validate_key_value_pairs(request)

    if key_value_errors:
        return response("{} key is missing".format(", ".join(key_value_errors)), 400)

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


@users_blueprint.route("/login", methods=["POST"])
def user_login():
    """User login endpoint"""
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    login = User().login(username, password)

    if login:
        login.update(
            {
                "token": jwt.encode(
                    {"user_id": login["username"]},
                    current_app.config["SECRET_KEY"],
                    algorithm="HS256",
                )
            }
        )

    return (
        response_with_data("login successful", login, 200)
        if login
        else response("authentication error!", 401)
    )


@users_blueprint.route("/users", methods=["GET"])
@jwt_required
def fetch_users():
    """Access a protected endpoint"""
    users = User().get_users()
    return response_with_data("OK", users, 200)
