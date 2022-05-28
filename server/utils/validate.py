from server.utils.errors import DateInputError
from datetime import date as dt


async def validate_date(data: str) -> dt:
    """validate data in row
    :entry: 
        :date: str -> "year.month"

    :return:
        :date: from datetime import date

    :raise:
        DateInputError
    """
    try:
        year, month = list(map(int, data.split('.')))
    except:
        raise DateInputError()
    return dt(year, month, 1)
