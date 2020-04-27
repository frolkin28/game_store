from flask import Flask
from flask_restful import Api

from application.database import db
from application import endpoints
from config import DevConfig


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevConfig)
    db.init_app(app)
    api = Api(app)
    register_endpoints(api)

    return app


def register_endpoints(api):
    api.add_resource(endpoints.UserApi, "/users")
