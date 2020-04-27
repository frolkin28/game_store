from flask_migrate import Migrate

from application import create_app
from application.database import db
from application import models

app = create_app()
migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run()
