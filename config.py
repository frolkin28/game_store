import enum
import os
import pathlib

BASE_DIR = pathlib.Path(__file__).parent


class RolesEnum(enum.Enum):
    user = 1
    manager = 2
    admin = 3


class BaseConfig:
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(BaseConfig):
    DEBUG = True
    ENV = "development"
    SQLALCHEMY_DATABASE_URI = f"postgresql://postgres:{os.getenv('POSTGRES_PASSWORD')}@localhost:{os.getenv('POSTGRES_PORT')}/game_store"
