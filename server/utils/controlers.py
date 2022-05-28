from datetime import date as dt
from datetime import datetime
from server.database.index import Index
from .validate import validate_date
from .commands import update_igpm, update_incc, update_ipca
from .errors import DateInputError
import logging


async def add_index(index: str, items_index: list) -> None:
    """add the indice if not exist else stop

    :entry:
        :index: str -> "ipca", "incc", "igpm"
        :items_index: list -> {"date":date,"index":str}

    """
    for row in items_index:
        if row.get('date'):
            try:
                date = await validate_date(row['date'])
                item = await Index.filter(date=date, name=index).first()
                if not item:
                    await Index.new(index, date, row['index'])
                else:
                    return
            except DateInputError:
                logging.warning('Date Invalid In Create Index')


async def update_database():
    """Update the database after verifi if not exist the indice of month previous"""

    date_now = datetime.now()
    date = dt(date_now.year, date_now.month-1, 1)  # recremet -1 in month

    item_ipca = await Index.filter(date=date, name='ipca').first()
    if not item_ipca:
        item_ipca = await update_ipca()
        item_ipca = item_ipca[::-1]
        await add_index('ipca', item_ipca)

    item_incc = await Index.filter(date=date, name='incc').first()
    if not item_incc:
        item_incc = await update_incc()
        item_incc = item_incc[::-1]
        await add_index('incc', item_incc)

    item_igpm = await Index.filter(date=date, name='igpm').first()
    if not item_igpm:
        item_igpm = await update_igpm()
        item_igpm = item_igpm[::-1]
        await add_index('igpm', item_igpm)
