import os
from flask import Flask
from instance.config import config
from .api.views.users import users_blueprint


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config[config_name])
    app.app_context().push()
    app.register_blueprint(users_blueprint, url_prefix="/api/v1/")

    return app
