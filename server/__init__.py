from flask import Flask
from server import database
from asyncio import run


def create_app():
    app = Flask(__name__)
    run(database.app_init())
    with app.app_context():
        from server import route #create routes with context

    return app
