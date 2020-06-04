import config
from application.database import db
from application import models
from run import app


def register_game_image(file_name, game_uuid):
    path = config.BASE_DIR / "images" / file_name
    print(path)
    game = db.session.query(models.Game).filter_by(uuid=game_uuid).first()
    print(game)


if __name__ == "__main__":
    file_name = "witcher.png"
    game_uuid = "02a319de-622b-4750-9bec-cd75f3802f42"
    register_game_image(file_name, game_uuid)
