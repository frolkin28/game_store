from flask import request
from flask_restful import Resource
from marshmallow.exceptions import ValidationError
from sqlalchemy.exc import IntegrityError, ProgrammingError

from application import schemas
from application import models
from application.database import db
from application.endpoints import auth

game_schema = schemas.GameSchema()
genre_schema = schemas.GenreSchema()


class GameApi(Resource):
    def get(self, uuid=None):
        if not uuid:
            return "", 400
        game = db.session.query(models.Game).filter_by(uuid=uuid).first()
        if not game:
            return "", 404
        return game_schema.dump(game), 200

    @auth.token_required
    def post(self):
        try:
            game = game_schema.load(request.json, session=db.session)
        except ValidationError as e:
            return {"message": str(e)}, 400
        try:
            db.session.add(game)
            db.session.commit()
        except IntegrityError:
            return {"message": "Game exists"}, 409
        return game_schema.dump(game), 201

    @auth.token_required
    def put(self, uuid):
        game = db.session.query(models.Game).filter_by(uuid=uuid).first()
        if not game:
            return "", 404
        game = game_schema.load(request.json, instance=game, session=db.session)
        db.session.add(game)
        db.session.commit()
        return game_schema.dump(game), 200

    @auth.token_required
    def delete(self, uuid):
        game = db.session.query(models.Game).filter_by(uuid=uuid).first
        if not game:
            return "", 404
        db.session.delete(game)
        db.session.commit()
        return "", 204


class GamesApi(Resource):
    def get(self):
        games = db.session.query(models.Game).all()
        return game_schema.dump(games, many=True), 200


class GenreApi(Resource):
    def get(self, title=None):
        if not title:
            return "", 400
        genre = db.session.query(models.Genre).filter_by(title=title).first()
        if not genre:
            return "", 404
        return genre_schema.dump(genre), 200

    @auth.token_required
    def post(self):
        try:
            genre = genre_schema.load(request.json, session=db.session)
        except ValidationError as e:
            return {"message": str(e)}, 400
        try:
            db.session.add(genre)
            db.session.commit()
        except IntegrityError:
            return {"message": "Genre exists"}, 409
        return genre_schema.dump(genre), 201


class InitSubgenres(Resource):
    @auth.token_required
    def post(self):
        try:
            genre_title = request.json.get("genre", None)

            if not genre_title:
                return "", 400
            genre = db.session.query(models.Genre).filter_by(title=genre_title).first()
            if not genre:
                return {"message": str(ValidationError("Invalid genre field"))}, 400

            subgenres_titles = request.json.get("subgenres", None)

            if not subgenres_titles:
                return {"message": str(ValidationError("Invalid subgenres field"))}, 400
            subgenres = (
                db.session.query(models.Genre)
                .filter(models.Genre.title.in_(subgenres_titles))
                .all()
            )
            if len(subgenres_titles) != len(subgenres):
                return "", 404
        except ProgrammingError:
            return "", 400
        genre.subgenres.extend(list(subgenres))
        db.session.commit()
        return "Subgenres assigned", 200
