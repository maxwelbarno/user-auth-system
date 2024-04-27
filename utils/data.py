import json

# user dummy data

user = json.dumps(dict(id=3, username="user", password="user123"))
wrong_login_credentials = json.dumps(dict(username="user", password="user12"))
user_data_with_missing_key = json.dumps(dict(username="user"))
user_data_with_blank_value = json.dumps(dict(username="user", password=""))
login_credentials_missing_key = json.dumps(dict(username="user"))
