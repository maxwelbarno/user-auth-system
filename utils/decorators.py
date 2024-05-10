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
            # Return True if user data is returned using data decrypted from JWT token
            isinstance(User().find_by_username(data["user_id"]), tuple)

        except Exception:
            return response("Invalid authorization header", 403)
        return func(*args, **kwargs)

    return decorated
