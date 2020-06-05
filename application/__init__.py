from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from application.database import db
from application import endpoints
from config import DevConfig


def create_app():
    app = Flask(__name__, static_folder=None)
    app.config.from_object(DevConfig)
    db.init_app(app)
    api = Api(app, prefix="/api/v1")
    register_endpoints(api)
    register_blueprints(app)
    CORS(app, resourses={r"/api/*": {"origins": ["http://localhost:8080"]}})

    return app


def register_endpoints(api):
    api.add_resource(endpoints.UserApi, "/user", "/user/<uuid>")
    api.add_resource(endpoints.GameApi, "/game", "/game/<uuid>")
    api.add_resource(endpoints.GamesApi, "/games")
    api.add_resource(endpoints.GenreApi, "/genre", "/genre/<title>")
    api.add_resource(endpoints.CommentApi, "/comment", "/comment/<game_id>")
    api.add_resource(endpoints.GameSearch, "/game/search/<search_value>")
    api.add_resource(endpoints.GameGenreFilter, "/game/filter/<filter_value>")
    api.add_resource(endpoints.GameAssignGenre, "/game_genre")
    api.add_resource(endpoints.GamePhoto, "/game_photo", "/game_photo/<id>")


def register_blueprints(app):
    app.register_blueprint(endpoints.login_blueprint)
