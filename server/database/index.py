from datetime import date as dt
from tortoise.models import Model
from tortoise.fields import IntField, DateField, CharField
from server.utils.errors import IndiceNameError, IndiceDataError


class Index(Model):
    id = IntField(pk=True)
    name = CharField(10)
    date = DateField(blank=True)
    index = CharField(50)

    @staticmethod
    async def new(name:str, date:dt, index:str) -> Model:
        """function to create row in table
        :entry:
            :name: str
            :date: date
            :index: str
        :return:
            :Index: Model
        
        :raise:
            IndiceNameError
            IndiceDateError
        
        """
        if name not in ('ipca', 'incc', 'igpm'):  # filter indices
            raise IndiceNameError()
        if not type(date) == dt:
            raise IndiceDataError()

        return await Index.create(name=name, date=date, index=index)

    def to_json(self) -> dict:
        return {"date": str(self.date), "index": self.index}
