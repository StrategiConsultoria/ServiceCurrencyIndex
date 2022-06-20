from server.database import db
from datetime import date as dt


class Index(db.Model):
    __tablename__ = 'indexs'
    ID = db.Column(db.Integer,primary_key=True)
    NAME = db.Column(db.String)
    DATE = db.Column(db.Date)
    INDEX = db.Column(db.Float)
    def __init__(self,name,date,index):
        super().__init__()
        if type(date) == dt:
            ...
        elif type(date) == str:
            date = list(map(int,date.split('-')))[::-1]
            date = dt(*date)
        self.NAME = name
        self.DATE = date
        self.INDEX = float(index)
    
    @property
    def date(self):
        return self.DATE.strftime('%d/%m/%Y')
    
    @property
    def index(self):
        return self.INDEX