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
