from ..db import Connection


class User:
    """User model"""

    def __init__(self):
        self.db = Connection()

    def create(self, username, password):
        """Save user details to users table in the database"""

        user = [username, password]
        self.db.create_table()
        self.db.insert(user)
        return {"username": username, "password": password}

    def login(self, username, password):
        """Login user using login credentials"""
        user = self.db.select_by_username(username)
        if password in user:
            return True
        else:
            return False
