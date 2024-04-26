from ..db import Connection
from passlib.hash import pbkdf2_sha256 as sha256


class User:
    """User model"""

    def __init__(self):
        self.db = Connection()

    def create(self, username, password):
        """Save user details to users table in the database"""
        passwordhash = sha256.hash(password)

        user = [username, passwordhash]
        self.db.create_table()
        self.db.insert(user)

    def login(self, username, password):
        """Login user using login credentials"""
        user = self.db.select_by_username(username)
        return sha256.verify(password, user[2])
