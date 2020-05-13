from flask_restful import Resource

from application import models, schemas
from application.database import db


game_schema = schemas.GameSchema()


class GameSearch(Resource):
    def get(self, search_value):
        result = models.Game.query.filter(
            models.Game.title.like(f"%{search_value}%")
        ).all()
        return game_schema.dump(result, many=True), 200


class GameGenreFilter(Resource):
    def get(self, filter_value):
        result = db.session.query(models.Genre).filter_by(title=filter_value).first()
        return game_schema.dump(result.games, many=True), 200
