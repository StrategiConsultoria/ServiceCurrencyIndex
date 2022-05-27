from server import create_app
import asyncio
from server.utils.controlers import update_database
from apscheduler.schedulers.background import BackgroundScheduler
import logging

logging.basicConfig( format='%(asctime)s - %(module)s - %(filename)s - %(message)s')

app =  create_app()

def start():
    asyncio.run(update_database())

sched = BackgroundScheduler(daemon=True)
sched.add_job(start,'cron', day_of_week='mon-fri', hour=0, minute=0)
sched.start()

if __name__ == '__main__':
    start()
    app.run()