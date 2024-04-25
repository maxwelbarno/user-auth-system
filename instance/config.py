class Config:
    """Parent configuration class"""

    DEBUG = False


class DevelopmentConfig(Config):
    """Development Configurations"""

    DEBUG = True
    TESTING = False
