from flask import request
from flask_restful import Resource
from marshmallow.exceptions import ValidationError
from sqlalchemy.exc import IntegrityError, ProgrammingError

from application import schemas
from application import models
from application.database import db
from application.endpoints import auth


comment_schema = schemas.CommentPostSchema()
comment_get_schema = schemas.CommentGetSchema()


class CommentApi(Resource):
    def get(self, game_id=None):
        if not game_id:
            return "", 404
        comments = db.session.query(models.Comment).filter_by(game_id=game_id).all()
        for i in comments:
            print(i.content)
        if not comments:
            return "", 404
        return comment_get_schema.dump(comments, many=True), 200

    @auth.token_required
    def post(self, user):
        try:
            comment = comment_schema.load(request.json, session=db.session)
        except ValidationError as e:
            return {"message": str(e)}, 400
        comment.author_id = user.id
        try:
            db.session.add(comment)
            db.session.commit()
        except IntegrityError:
            return {"message": "Comment exists"}, 409
        return comment_schema.dump(comment), 201
