from flask import Flask
from server import database
from apscheduler.schedulers.background import BackgroundScheduler
from server.utils.controlers import update_database
from asyncio import run
import logging
import asyncio
import dotenv
from server.utils import check_env

def create_app():
    dotenv.load_dotenv('index.env')
    check_env()
    logging.info('Start App')
    app = Flask(__name__)
    run(database.app_init())
    with app.app_context():
        from server import route #create routes with context

    sched = BackgroundScheduler(daemon=True)
    sched.add_job(lambda *args:asyncio.run(update_database()), 'cron', day_of_week='mon-fri', hour=0, minute=0)
    sched.start()

    return app
