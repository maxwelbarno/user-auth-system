from flask import Flask
from instance.config import DevelopmentConfig

from .api.views.users import users_blueprint


def create_app():

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(DevelopmentConfig())
    app.secret_key = "sweetsecret"
    app.config["MYSQL_USER"] = "admin"
    app.config["MYSQL_PASSWORD"] = "admin123"
    # push application context for tests
    app.app_context().push()
    app.register_blueprint(users_blueprint, url_prefix="/api/v1/")

    return app
