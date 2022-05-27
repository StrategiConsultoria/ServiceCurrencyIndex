from flask import Flask
from server import database
from asyncio import run
import logging


def create_app():
    logging.info('Start App')
    app = Flask(__name__)
    run(database.app_init())
    with app.app_context():
        from server import route #create routes with context

    return app
