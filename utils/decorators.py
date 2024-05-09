import jwt
from functools import wraps
from flask import request, current_app
from app.api.models.user import User
from .responses import response


def jwt_required(func):

    @wraps(func)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]
        else:
            return response("Authorization header missing", 403)
        try:
            data = jwt.decode(
                token, current_app.config["SECRET_KEY"], algorithms=["HS256"]
            )
            current_user = User().find_by_username(data["user_id"])
            if current_user is None:
                return response("Authorization header missing", 403)

        except Exception:
            return response("Invalid authorization header", 403)
        return func(*args, **kwargs)

    return decorated
