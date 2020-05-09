import uuid
from werkzeug.security import generate_password_hash

import config
from application.database import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(36), unique=True)
    first_name = db.Column(db.String(60))
    second_name = db.Column(db.String(60))
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(94))
    role = db.Column(
        db.Enum(config.RolesEnum), nullable=False, default=config.RolesEnum.user.name
    )

    def __init__(self, first_name, second_name, email, password):
        self.uuid = str(uuid.uuid4())
        self.first_name = first_name
        self.second_name = second_name
        self.email = email
        self.password = generate_password_hash(password)


game_genre = db.Table(
    "game_genre",
    db.Column("game_id", db.Integer, db.ForeignKey("games.id"), primary_key=True),
    db.Column("genre_id", db.Integer, db.ForeignKey("genres.id"), primary_key=True),
)


class Game(db.Model):
    __tablename__ = "games"

    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(36), unique=True)
    title = db.Column(db.String(255))
    details = db.Column(db.Text())
    price = db.Column(db.Float())
    genres = db.relationship(
        "Genre", secondary=game_genre, backref=db.backref("games", lazy="dynamic")
    )

    def __init__(self, title, details, price):
        self.uuid = str(uuid.uuid4())
        self.title = title
        self.details = details
        self.price = price


genre_subgenre = db.Table(
    "genre_subgenre",
    db.Column("genre_id", db.Integer, db.ForeignKey("genres.id")),
    db.Column("subgenre_id", db.Integer, db.ForeignKey("genres.id")),
)


class Genre(db.Model):
    __tablename__ = "genres"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True)
    subgenres = db.relationship(
        "Genre",
        secondary=genre_subgenre,
        primaryjoin=("Genre.id==genre_subgenre.c.subgenre_id"),
        secondaryjoin=("Genre.id==genre_subgenre.c.genre_id"),
    )


comment_reply = db.Table(
    "comment_reply",
    db.Column("comment_id", db.Integer, db.ForeignKey("comments.id")),
    db.Column("reply_id", db.Integer, db.ForeignKey("comments.id")),
)


class Comment(db.Model):
    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text())
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    author = db.relationship("User")
    game_id = db.Column(db.Integer, db.ForeignKey("games.id"))
    game = db.relationship("Game")
    replies = db.relationship(
        "Comment",
        secondary=comment_reply,
        primaryjoin=("Comment.id==comment_reply.c.reply_id"),
        secondaryjoin=("Comment.id==comment_reply.c.comment_id"),
    )


cart_game = db.Table(
    "cart_game",
    db.Column("game_id", db.Integer, db.ForeignKey("games.id")),
    db.Column("cart_id", db.Integer, db.ForeignKey("cart.id")),
)


class Cart(db.Model):
    __tablename__ = "cart"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user = db.relationship("User")
    games = db.relationship("Game", secondary=cart_game, lazy="dynamic")


class GamePhoto(db.Model):
    __tablename__ = "game_photo"

    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(255), unique=True)
    url = db.Column(db.String(255))
    game_id = db.Column(db.Integer, db.ForeignKey("games.id"))
    game = db.relationship("Game")


class AvatarImage(db.Model):
    __tablename__ = "avatar_image"

    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(255), unique=True)
    url = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user = db.relationship("User")
