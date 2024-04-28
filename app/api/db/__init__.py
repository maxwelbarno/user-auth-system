from flask import current_app
import mysql.connector


class Connection:
    """Database connection class"""

    def __init__(self):

        self.password = current_app.config["MYSQL_PASSWORD"]
        self.user = current_app.config["MYSQL_USER"]
        self.db = current_app.config["MYSQL_DB"]
        self.host = current_app.config["MYSQL_HOST"]

        # Create database connection
        self.conn = mysql.connector.connect(
            user=self.user, password=self.password, database=self.db, host=self.host
        )
        # Create cursor
        self.cursor = self.conn.cursor()

    def create_table(self):
        """Create a table in the database"""
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS accounts(id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255),password \
                VARCHAR(255))"
        )
        self.conn.commit()

    def drop_table(self):
        """Drop table from the database"""
        self.cursor.execute("DROP TABLE accounts")
        self.conn.commit()

    def insert(self, data):
        """Insert record to table in the database"""
        self.cursor.execute(
            "INSERT INTO accounts (username, password) VALUES(%s,%s)",
            data,
        )
        self.conn.commit()

    def select_by_username(self, username):
        """select a record from the database table based on its username"""
        self.cursor.execute("SELECT * FROM accounts WHERE username=%s", [username])
        record = self.cursor.fetchone()
        return record
