import os
from app import BASEDIR

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SESSION_COOKIE_SECURE = True

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    SESSION_COOKIE_SECURE = False
    SECRET_KEY = "B\xb2?.\xdf\x9f\xa7m\xf8\x8a%\xf7\xc4\xfa\x91"
