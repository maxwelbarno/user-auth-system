import os
from unittest import TestCase
from app import create_app
from app.api.db import Connection
from instance.config import config

config_name = os.environ.get("FLASK_ENV", "testing")


class BaseTestCase(TestCase):
    def setUp(self):
        self.app = create_app(config_name)
        self.app.config.from_object(config[config_name])
        self.client = self.app.test_client()
        conn = Connection()
        conn.create_table()

    def register(self, data):
        """register user method"""
        return self.client.post(
            "api/v1/register", data=data, content_type="application/json"
        )

    def login(self, data):
        """login user method"""
        return self.client.post(
            "api/v1/login", data=data, content_type="application/json"
        )

    def fetch_users(self, token):
        """login user method"""
        return self.client.get(
            "api/v1/users",
            headers={"Authorization": "Bearer {}".format(token)},
        )

    def fetch_users_without_jwt(self):
        """login user method"""
        return self.client.get("api/v1/users")

    def tearDown(self):
        with self.app.app_context():
            conn = Connection()
            conn.drop_table()
