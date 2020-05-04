from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields

from application import models


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = models.User
        exclude = ("id",)
        load_instance = True


class UserGetSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = models.User
        exclude = ("id", "password")
        load_instance = True


class GenreSchema(SQLAlchemyAutoSchema):
    subgenres = fields.Nested("self", many=True)
    games = fields.Nested("GameSchema", many=True)

    class Meta:
        model = models.Genre
        load_instance = True


class GameSchema(SQLAlchemyAutoSchema):
    genres = fields.Nested(GenreSchema, many=True)

    class Meta:
        model = models.Game
        exclude = ("id",)
        load_instance = True


class CommentPostSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = models.Comment
        load_instance = True


class CommentGetSchema(SQLAlchemyAutoSchema):
    author = fields.Nested(UserGetSchema, many=True)
    game = fields.Nested(GameSchema, many=True)
    replies = fields.Nested("self", many=True)

    class Meta:
        model = models.Comment
        exclude = ("author_id", "game_id")
        load_instance = True


class CartSchema(SQLAlchemyAutoSchema):
    games = fields.Nested(GameSchema, many=True)
    user = fields.Nested(UserGetSchema)

    class Meta:
        model = models.Cart
