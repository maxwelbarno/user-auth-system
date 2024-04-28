import os


class Config(object):
    """Parent configuration class"""

    DEBUG = False


class DevelopmentConfig(Config):
    """Development Configurations"""

    DEBUG = True
    TESTING = False
    MYSQL_DB = os.environ.get("MYSQL_DB")


class TestingConfig(Config):
    """Test Configurations"""

    TESTING = True
    DEBUG = True
    MYSQL_DB = "mysql_user_auth_test"
