import os


class Config(object):
    """Parent configuration class"""

    DEBUG = False
    MYSQL_USER = os.environ.get("MYSQL_USER")
    MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD")
    SECRET_KEY = os.environ.get("SECRET_KEY")
    MYSQL_DB = os.environ.get("MYSQL_DB")
    MYSQL_HOST = os.environ.get("MYSQL_HOST")


class ProductionConfig(Config):
    """Production Configurations"""

    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    """Development Configurations"""

    DEBUG = True
    TESTING = False


class TestingConfig(DevelopmentConfig):
    """Test Configurations"""

    TESTING = True


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
}
