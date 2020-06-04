from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from marshmallow_enum import EnumField

from application import models
import config


class UserSchema(SQLAlchemyAutoSchema):
    role = EnumField(config.RolesEnum)

    class Meta:
        model = models.User
        exclude = ("id",)
        load_instance = True


class UserGetSchema(SQLAlchemyAutoSchema):
    role = EnumField(config.RolesEnum)

    class Meta:
        model = models.User
        exclude = ("id", "password")
        load_instance = True


class GenreSchema(SQLAlchemyAutoSchema):
    parent_genre = fields.Nested("self")
    games = fields.Nested("GameSchema", many=True)

    class Meta:
        include_fk = True
        model = models.Genre
        load_instance = True


class GenreGetSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = models.Genre
        load_instance = True
        exclude = ("id", "games", "parent_genre")


class GamePhotoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = models.GamePhoto
        exclude = ("game", "game_id")


class GameSchema(SQLAlchemyAutoSchema):
    genres = fields.Nested(GenreGetSchema, many=True)
    game_photo = fields.Nested(GamePhotoSchema)

    class Meta:
        model = models.Game
        exclude = ("id",)
        load_instance = True


class CommentPostSchema(SQLAlchemyAutoSchema):
    class Meta:
        include_fk = True
        model = models.Comment
        load_instance = True


class CommentGetSchema(SQLAlchemyAutoSchema):
    author = fields.Nested(UserGetSchema)
    game = fields.Nested(GameSchema)
    replies = fields.Nested("self", many=True)

    class Meta:
        model = models.Comment
        exclude = ("author_id", "game_id", "id")
        load_instance = True


class CartSchema(SQLAlchemyAutoSchema):
    games = fields.Nested(GameSchema, many=True)
    user = fields.Nested(UserGetSchema)

    class Meta:
        model = models.Cart
