from datetime import date as dt
from datetime import datetime
from functools import partial

from apscheduler.schedulers.background import BackgroundScheduler
from server.database import db
from server.database.models.index import Index
from server.scrape.ipeadata import IpeadataScrape


def add_indexs(name, serid):
    """register index in database
    :entry:
        :name: str -> name to index
        :serid: int -> serid to scrape Ipeadata
    """
    name = name.upper()
    print(f'Start {name}')
    now = datetime.now()
    news_count = 0
    date_month_previous = dt(now.year, now.month-1, 1)
    index_month_previous = Index.query.filter_by(
        DATE=date_month_previous, NAME=name).first()
    if index_month_previous == None:
        print(f'Start Scrapy {name}')
        scrape = IpeadataScrape(serid)
        indexs = list(scrape.start())
        for index_data in indexs:
            index = index_data['index']
            date = dt(*list(map(int, index_data['date'].split('-')))[::-1])
            if Index.query.filter_by(DATE=date, NAME=name).first():
                print(f'Stop {name} - {news_count}')
                return
            else:
                try:
                    index = float(index)
                except Exception:
                    index = 0.0
                db.session.add(Index(name, date, index))
                db.session.commit()
                news_count += 1
    print(f'Stop {name} - {news_count}')


def check_indexs(app):
    print('Start Check')
    with app.app_context():
        add_indexs('ipca', 36482)
        add_indexs('incc', 33596)
        add_indexs('igpm', 37796)
        add_indexs('v_incc',39618)
    print('Closed Check')


def start_schedule(app):
    sched = BackgroundScheduler(daemon=True, timezone='America/Sao_Paulo')
    sched.add_job(partial(check_indexs, app), 'cron',
                  day_of_week='mon-fri', hour=9, minute=20)
    sched.start()
