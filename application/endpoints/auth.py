import datetime
import jwt
from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash

from application import models
from config import BaseConfig, RolesEnum
from application.database import db

login_blueprint = Blueprint("login", __name__)


@login_blueprint.route("/login")
def login():
    email = request.authorization.get("username", "")
    password = request.authorization.get("password", "")
    user = db.session.query(models.User).filter_by(email=email).first()
    if not user or check_password_hash(user.password, password):
        return "", 401, {"WWW-Authenticate": 'Basic realm="Authentication required"'}
    token = jwt.encode(
        {
            "user_id": user.uuid,
            "exp": datetime.datetime.now() + datetime.timedelta(hours=1),
        },
        BaseConfig.SECRET_KEY,
    )
    return jsonify({"token": token.decode("utf-8")})


@login_blueprint.route("/logout")
def logout():
    return jsonify({"token": ""})


def token_required(f):
    def wrapper(self, *args, **kwargs):
        token = request.headers.get("token", "")
        if not token:
            return (
                "",
                401,
                {"WWW-Authenticate": 'Basic realm="Authentication required"'},
            )
        try:
            uuid = jwt.decode(token, BaseConfig.SECRET_KEY)["user_id"]
        except (KeyError, jwt.ExpiredSignatureError):
            return (
                "",
                401,
                {"WWW-Authenticate": 'Basic realm="Authentication required"'},
            )
        user = db.session.query(models.User).filter_by(uuid=uuid).first()
        if not user:
            return (
                "",
                401,
                {"WWW-Authenticate": 'Basic realm="Authentication required"'},
            )
        return f(self, user, *args, **kwargs)

    return wrapper


def managers_only(f):
    def wrapper(self, user, *args, **kwargs):
        if user.role != RolesEnum.manager:
            return "", 405
        return f(self, user, *args, **kwargs)

    return wrapper


def admins_only(f):
    def wrapper(self, user, *args, **kwargs):
        if user.role != RolesEnum.admin:
            return "", 405
        return f(self, user, *args, **kwargs)

    return wrapper
