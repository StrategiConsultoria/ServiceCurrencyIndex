from datetime import date as dt
from tortoise.models import Model
from tortoise.fields import IntField, DateField, CharField
from server.utils.errors import IndexDateError


class Index(Model):
    id = IntField(pk=True)
    name = CharField(10)
    date = DateField(blank=True)
    index = CharField(50)

    @staticmethod
    async def new(name: str, date: dt, index: str) -> Model:
        """function to create row in table

        :entry:
            :name: str
            :date: date
            :index: str

        :return:
            :Index: Model

        :raise:
            IndexDateError

        """
        if not type(date) == dt:
            raise IndexDateError()

        return await Index.create(name=name, date=date, index=index)

    def to_json(self) -> dict:
        return {"date": str(self.date), "index": self.index}

    @property
    def get_date_format(self):
        return self.date.strftime('%d/%m/%Y')
        
    @property
    def get_index_format(self):
        return self.index.replace(',', '.')
