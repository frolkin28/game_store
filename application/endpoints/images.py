import base64
import config

from flask import request, jsonify
from flask_restful import Resource
from application.database import db
from application import models


class GamePhoto(Resource):
    def get(self, id=None):
        if not id:
            return "", 404
        image = db.session.query(models.GamePhoto).filter_by(id=id).first()
        image_path = image.path
        with open(image_path, "rb") as f:
            data = base64.b64encode(f.read()).decode('ascii')
        res = {'image': data}
        return res, 200

    def post(self):
        uuid = request.json["game_uuid"]
        file_name = request.json["file_name"]
        game_id = db.session.query(models.Game).filter_by(uuid=uuid).first().id
        path = str(config.BASE_DIR / "images" / file_name)
        # game_photo = models.GamePhoto(path=path, game_id=game_id)
        # db.session.add(game_photo)
        # db.session.commit()
        return 200

    def put(self):
        id = request.json["id"]
        file_name = request.json["file_name"]
        game_photo = db.session.query(models.GamePhoto).filter_by(id=id).first()
        path = str(config.BASE_DIR / "images" / file_name)
        game_photo.path = path
        game_photo.url = f'/game_photo/{id}'
        db.session.add(game_photo)
        db.session.commit()
        return 200
