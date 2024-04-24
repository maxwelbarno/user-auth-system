from flask import Flask, request, render_template, session
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)
app.secret_key = "sweetsecret"
app.config["MYSQL_USER"] = "admin"
app.config["MYSQL_PASSWORD"] = "admin123"
app.config["MYSQL_DB"] = "mysql_user_auth"

mysql = MySQL(app)


@app.route("/")
def hello():
    return "Hello world!"


@app.route("/register", methods=["POST", "GET"])
def register():
    message = ""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("DROP TABLE accounts")
        cursor.execute(
            "CREATE TABLE accounts(id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255),password VARCHAR(255))"
        )
        cursor.execute("SELECT * FROM accounts WHERE username=%s", (username,))
        account = cursor.fetchone()
        if account:
            message = "Account already exists!"

        else:
            cursor.execute(
                "INSERT INTO accounts (username, password) VALUES(%s,%s)",
                [username, password],
            )
            mysql.connection.commit()
            message = "user successfully registered!"
    return render_template("register.html", message=message)


@app.route("/login", methods=["POST", "GET"])
def login():
    message = ""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            "SELECT * FROM accounts WHERE username=%s AND password=%s",
            (
                username,
                password,
            ),
        )

        account = cursor.fetchone()
        if account:
            session["loggedin"] = True
            session["id"] = account["id"]
            session["username"] = account["username"]
            message = "User logged in successfully!"
            return render_template("index.html", message=message)
        else:
            message = "Incorrect username or password"
    return render_template("login.html", message=message)
