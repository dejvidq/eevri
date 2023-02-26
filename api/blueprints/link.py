from flask import Blueprint

link = Blueprint("link", __name__)


@link.route("/")
def root():
    return {"success": "Correct"}, 200
