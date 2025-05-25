[![Build and Deploy](https://github.com/codetaskmaster/user-auth-system/actions/workflows/main.yaml/badge.svg?branch=main)](https://github.com/codetaskmaster/user-auth-system/actions/workflows/main.yaml)
[![Coverage Status](https://coveralls.io/repos/github/codetaskmaster/user-auth-system/badge.svg)](https://coveralls.io/github/codetaskmaster/user-auth-system)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=maxwelbarno_user-auth-system&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=maxwelbarno_user-auth-system)
[![Maintainability](https://api.codeclimate.com/v1/badges/3e0cb305a16630b03c30/maintainability)](https://codeclimate.com/github/maxwelbarno/user-auth-system/maintainability)

# Setup

To run the project locally

1. Clone this repository
2. From the terminal, navigate to the root directory of the cloned project
3. Create virtual environment
4. Install dependencies in the `requirements.txt` file

   `pip install -r requirements.txt`

### Run application

1. Create `.env` file in the root directory and assign the following environment variables

```
FLASK_DEBUG=1
FLASK_ENV=
MYSQL_PASSWORD=
MYSQL_USER=
MYSQL_DB=
MYSQL_HOST=
SECRET_KEY=
```

#### Using inbuilt Werkzeug Server

a. From the terminal in the project root directory, run the following command

`flask --app run.py  run`

#### Using Gunicorn Server

2. Create gunicorn configuration file `gunicorn.conf.py` in the root directory and add the following environment variables

```
import os

os.environ["FLASK_ENV"] =
os.environ["MYSQL_USER"] =
os.environ["MYSQL_PASSWORD"] =
os.environ["MYSQL_DB"] =
os.environ["SECRET_KEY"] =

bind = "0.0.0.0:5000"
wsgi_app = "run:app"
```

b. From the terminal in the project root directory, run the following command

`gunicorn --config gunicorn.conf.py`

### Dockerize application

1. Open terminal in the root directory
2. Create `production.env` file in the root directory and assign the following environment variables

```
FLASK_DEBUG=1
FLASK_ENV=
MYSQL_PASSWORD=
MYSQL_USER=
MYSQL_DB=
MYSQL_HOST=
SECRET_KEY=
```

3. Setup docker

   `docker login`

4. Navigate to the application's root directory

5. Build docker image

   `docker build --tag user-auth-system .`

6. Start docker application

   `docker compose up --detach --build`

   NB: The above command builds, recreates, starts and attaches to all containers defined in `docker-compose.yaml` file. It fires the multi-container application up and running.

7. To stop docker application, run the following command from terminal

   `docker compose down`
