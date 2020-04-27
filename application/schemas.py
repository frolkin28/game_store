from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from application import models


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = models.User
        exclude = ("id",)
        load_instance = True


class GameSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = models.Game
        exclude = ("id",)
        load_instance = True
