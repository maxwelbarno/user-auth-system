import json
from .base_test import BaseTestCase
from utils.data import (
    user,
    wrong_login_credentials,
    user_data_with_missing_key,
    user_data_with_blank_value,
)


class UserTestCase(BaseTestCase):
    def test_register_user(self):
        """Test register user endpoint"""
        response = super().register(user)
        response_content = json.loads(response.data.decode())
        self.assertTrue(response_content["status"] == 201)
        self.assertTrue(response_content["message"] == "user registered successfully!")

    def test_register_user_failure_missing_key_error(self):
        """Test user login endpoint"""
        super().register(user)
        response = super().register(user_data_with_missing_key)
        response_content = json.loads(response.data.decode())
        self.assertTrue(response_content["status"] == 400)

    def test_register_user_failure_blank_value_error(self):
        """Test user login endpoint"""
        super().register(user)
        response = super().register(user_data_with_blank_value)
        response_content = json.loads(response.data.decode())
        self.assertTrue(response_content["status"] == 400)

    def test_register_existing_user(self):
        """Test user login endpoint"""
        super().register(user)
        response = super().register(user)
        response_content = json.loads(response.data.decode())
        self.assertTrue(response_content["status"] == 400)

    def test_login_user(self):
        """Test user login endpoint"""
        super().register(user)
        response = super().login(user)
        response_content = json.loads(response.data.decode())
        self.assertTrue(response_content["status"] == 200)

    def test_login_failure(self):
        """Test user login endpoint"""
        super().register(user)
        response = super().login(wrong_login_credentials)
        response_content = json.loads(response.data.decode())
        self.assertTrue(response_content["status"] == 401)

    def test_get_users(self):
        """Test user login endpoint"""
        super().register(user)
        login_response = super().login(user)
        login_response_content = json.loads(login_response.data.decode())
        token = login_response_content["data"]["token"]
        response = super().fetch_users(token)
        response_content = json.loads(response.data.decode())
        self.assertTrue(response_content["status"] == 200)
        self.assertTrue(response_content["message"] == "OK")
        self.assertTrue(isinstance(response_content["data"], list))

    def test_get_users_with_invalid_auth_token(self):
        """Test user login endpoint"""
        super().register(user)
        login_response = super().login(user)
        login_response_content = json.loads(login_response.data.decode())
        token = login_response_content["data"]["token"]
        response = super().fetch_users(token.lower())
        response_content = json.loads(response.data.decode())
        self.assertTrue(response_content["status"] == 403)
        self.assertTrue(response_content["message"] == "Invalid authorization header")
