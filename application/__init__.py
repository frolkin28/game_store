from flask import Flask
from flask_restful import Api

from application.database import db
from application import endpoints
from application.endpoints import login_blueprint
from config import DevConfig


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevConfig)
    db.init_app(app)
    api = Api(app, prefix="/api/v1")
    register_endpoints(api)
    register_blueprints(app)

    return app


def register_endpoints(api):
    api.add_resource(endpoints.UserApi, "/user", "/user/<uuid>")
    api.add_resource(endpoints.GameApi, "/game", "/game/<uuid>")
    api.add_resource(endpoints.GamesApi, "/games")
    api.add_resource(endpoints.GenreApi, "/genre", "/genre/<title>")
    api.add_resource(endpoints.InitSubgenres, "/subgenres")
    api.add_resource(endpoints.CommentApi, "/comment", "/comment/<game_id>")


def register_blueprints(app):
    app.register_blueprint(login_blueprint)
