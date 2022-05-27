from datetime import date as dt
from tortoise.models import Model
from tortoise.fields import IntField, DateField, CharField
from server.utils.errors import IndiceNameError, IndiceDataError


class Indice(Model):
    id = IntField(pk=True)
    name = CharField(10)
    date = DateField(blank=True)
    indice = CharField(50)

    @staticmethod
    async def new(name:str, date:dt, indice:str) -> Model:
        """function to create row in table
        :entry:
            :name: str
            :date: date
            :indice: str
        :return:
            :Indice: Model
        
        :raise:
            IndiceNameError
            IndiceDateError
        
        """
        if name not in ('ipca', 'incc', 'igpm'):  # filter indices
            raise IndiceNameError()
        if not type(date) == dt:
            raise IndiceDataError()

        return await Indice.create(name=name, date=date, indice=indice)

    def to_json(self) -> dict:
        return {"date": str(self.date), "indice": self.indice}
