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

    class Meta:
        model = models.Genre
        load_instance = True


class GameSchema(SQLAlchemyAutoSchema):
    genres = fields.Nested(GenreSchema)

    class Meta:
        model = models.Game
        exclude = ("id",)
        load_instance = True
