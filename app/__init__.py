from flask import Flask
from instance.config import DevelopmentConfig

from .api.views.users import user


def create_app():

    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(DevelopmentConfig)
    app.secret_key = "sweetsecret"
    app.config["MYSQL_USER"] = "admin"
    app.config["MYSQL_PASSWORD"] = "admin123"
    app.config["MYSQL_DB"] = "mysql_user_auth"
    app.register_blueprint(user, url_prefix="/api/v1/")

    return app
