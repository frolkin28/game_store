from flask import Blueprint, render_template

import config

index = Blueprint(
    "index",
    __name__,
    template_folder=str(config.BASE_DIR / "templates"),
    static_folder=str(config.BASE_DIR / "static"),
)


@index.route("/")
def main():
    return render_template("index.html")
