import uuid
from werkzeug.security import generate_password_hash

from application.database import db


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(36), unique=True)
    first_name = db.Column(db.String(60))
    second_name = db.Column(db.String(60))
    email = db.Column(db.String(120))
    password = db.Column(db.String(94))

    def __init__(self, first_name, second_name, email, password):
        self.uuid = str(uuid.uuid4())
        self.first_name = first_name
        self.second_name = second_name
        self.email = email
        self.password = generate_password_hash(password)


class Game(db.Model):
    __tablename__ = "game"

    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(36), unique=True)
    title = db.Column(db.String(255))
    details = db.Column(db.Text())
    price = db.Column(db.Float())

    def __init__(self, title, details, price):
        self.uuid = str(uuid.uuid4())
        self.title = title
        self.details = details
        self.price = price
