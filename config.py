import os
import pathlib


BASE_DIR = pathlib.Path(__file__).parent


class BaseConfig:
    SECRET_KEY = os.getenv('SECRET_KEY')
    # SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(BaseConfig):
    DEBUG = True
    ENV = 'development'
    # SQLALCHEMY_DATABASE_URI = ''
