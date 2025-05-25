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

    def find_by_username(self, username):
        """Find user in the database table using username"""
        self.db.create_table()
        return self.db.select_by_username(username)

    def login(self, username, password):
        """Login user using login credentials"""
        record = self.find_by_username(username)
        if record:
            # unpacking the record tuple
            record_id, record_username, record_password = record
            if sha256.verify(password, record_password):
                user = dict(id=int(record_id), username=record_username)
                return user
        else:
            return False

    def get_users(self):
        """Fetch all users in the database table"""
        records = self.db.select_all()
        users = []
        for record in records:
            # unpacking the records list but don't unpack password field
            record_id, record_username, _ = record
            user = dict(id=int(record_id), username=record_username)
            users.append(user)
        return users
