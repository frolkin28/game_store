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


def check_comment_owner(user, comment):
    return comment.author.uuid == user.uuid


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

    @auth.token_required
    def put(self, user, id=None):
        if not id:
            return "", 400
        comment = models.Comment.query.get(id)
        if not comment or not check_comment_owner(user, comment):
            return "", 404
        comment = comment_schema.load(
            request.json, instance=comment, session=db.session
        )
        db.session.add(comment)
        db.session.commit()
        return comment_schema.dump(comment), 200

    @auth.token_required
    def delete(self, user, id=None):
        if not id:
            return "", 400
        comment = models.Comment.query.get(id)
        if not comment or not check_comment_owner(user, comment):
            return "", 404
        db.session.delete(comment)
        db.session.commit()
        return "", 204
