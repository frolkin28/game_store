from flask import request
from flask_restful import Resource
from marshmallow.exceptions import ValidationError
from sqlalchemy.exc import IntegrityError

from application import schemas
from application import models
from application.database import db


user_schema = schemas.UserSchema()
user_get_schema = schemas.UserGetSchema()


class UserApi(Resource):
    def get(self, uuid=None):
        if not uuid:
            return "", 404
        user = db.session.query(models.User).filter_by(uuid=uuid).first()
        if not user:
            return "", 404
        return user_get_schema.dump(user), 200

    def post(self):
        try:
            user = user_schema.load(request.json, session=db.session)
        except ValidationError as e:
            return {"message": str(e)}, 400
        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            return {"message": "User exists"}, 409
        return user_schema.dump(user), 201
