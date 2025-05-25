import os

os.environ["FLASK_ENV"] = "production"
os.environ["MYSQL_USER"] = "admin"
os.environ["MYSQL_PASSWORD"] = "admin123"
os.environ["MYSQL_DB"] = "user_auth"
os.environ["SECRET_KEY"] = "sweet-secret"

bind = "0.0.0.0:5000"
wsgi_app = "run:app"
