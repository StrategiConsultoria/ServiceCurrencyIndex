from flask import Flask

from server.database import db
from server.utils.schedule import start_schedule,check_indexs


def create_app():
    app = Flask(__name__)
    app.secret_key = 'secret'
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    with app.app_context():
        db.init_app(app)
        db.create_all()
        from server.routes import ipeadata
        check_indexs(app)
        start_schedule(app)

    return app
