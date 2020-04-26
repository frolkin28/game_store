from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from application.endpoints import UserApi
from config import DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy()
migrate = Migrate(app, db)
api = Api(app)

api.add_resource(UserApi, '/users')
