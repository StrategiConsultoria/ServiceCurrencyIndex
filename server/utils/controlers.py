from datetime import date as dt
from datetime import datetime
from server.database.indices import Indice
from .validate import validate_date
from .commands import update_igpm, update_incc, update_ipca


async def add_indice(indice:str, item_indice:list) -> None:
    """add the indice if not exist else stop
    
    :entry:
        :indice: str -> ["ipca","incc","igpm"]
        :item_indice: list -> {"date":date,"indice":str}

    """
    for row in item_indice:
        if row.get('date'):
            date = await validate_date(row['date'])
            item = await Indice.filter(date=date, name=indice).first()
            if not item:
                await Indice.new(indice, date, row['indice'])
            else:
                return


async def update_database():
    """Update the database after verifi if not exist the indice of month previous"""
    """Atualiza o banco de dados apos verificar se nao existe o indice do mes passado"""

    date_now = datetime.now()
    date = dt(date_now.year, date_now.month-1, 1)#recremet -1 in month

    item_ipca = await Indice.filter(date=date, name='ipca').first()
    if not item_ipca:
        item_ipca = await update_ipca()
        item_ipca = item_ipca[::-1]
        await add_indice('ipca', item_ipca)

    item_incc = await Indice.filter(date=date, name='incc').first()
    if not item_incc:
        item_incc = await update_incc()
        item_incc = item_incc[::-1]
        await add_indice('incc', item_incc)

    item_igpm = await Indice.filter(date=date, name='igpm').first()
    if not item_igpm:
        item_igpm = await update_igpm()
        item_igpm = item_igpm[::-1]
        await add_indice('igpm', item_igpm)
