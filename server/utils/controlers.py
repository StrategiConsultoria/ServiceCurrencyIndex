from datetime import date as dt
from datetime import datetime
from server.database.index import Index
from .validate import validate_date
from .commands import command
from .errors import DateInputError
import logging
import os
import json


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
                logging.warning(MessageLog['date_invalide_new_index'].value)

async def update_database() -> None:
    """Update the database after verifi if not exist the indice of month previous"""

    date_now = datetime.now()
    date = dt(date_now.year, date_now.month-1, 1)  # recremet -1 in month

    indexs = json.loads(os.environ.get('INDEXS','{}'))
    for index, serid in indexs.items():
        index_item = await Index.filter(date=date, name=index).first()
        if not index_item:
            items = await command(serid)
            items = items[::-1]
            await add_index(index, items)