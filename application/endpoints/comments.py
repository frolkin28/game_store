from flask import request
from flask_restful import Resource
from marshmallow.exceptions import ValidationError
from sqlalchemy.exc import IntegrityError, ProgrammingError

from application import schemas
from application import models
from application.database import db


class CommentApi(Resource):
    def post(self):
        pass
