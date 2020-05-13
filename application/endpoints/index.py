from flask import Blueprint, render_template

import config

index = Blueprint("index", __name__, template_folder=str(config.BASE_DIR / "templates"))


@index.route("/")
def main():
    return render_template("base.html")
