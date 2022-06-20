from flask import Flask

from server import database
from server.utils.schedule import check_indexs, start_schedule


def create_app():
    app = Flask(__name__)
    app.secret_key = 'secret'
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    with app.app_context():
        database.init_app(app)
        from server.routes import ipeadata
        check_indexs(app)
        start_schedule(app)

    return app
