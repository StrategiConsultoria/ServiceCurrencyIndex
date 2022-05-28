from datetime import datetime
from .errors import DateInputError
from .message import Message


def capture_year(request, arg: str) -> int:
    """_capture args in request and return year

    :entry:
        :request: Request -> Flask
        :arg: str > "2022"

    :return:
        :int: 2022

    :raise:
        DateInputError
    """
    year: str = request.args.get(arg, None)  # capture
    date_now = datetime.now()  # get now

    if year:
        if year.isnumeric():
            year = int(year)

            if year < 1000:  # year cannot be less than 1000
                year = 1000

            if not year <= date_now.year:  # year cannot be greater than the current year
                raise DateInputError(Message[arg+'_future'].value)
        else:
            raise DateInputError(Message[arg+'_not_number'].value)
    else:
        year = date_now.year

    return year


def capture_month(request, arg: str) -> int:
    """ capture args in request and return month

    :entry:
        :request: Request -> Flask
        :arg: str > "05"

    :return:
        int: 5

    :raise:
        MonthInputError
    """
    month: str = request.args.get(arg, None)
    if month:
        if month.isnumeric():
            month = int(month)

            if month < 1:  # month cannot be less than 1
                month = 1

            if month > 12:  # month cannot be greater than 12
                month = 12

        else:
            raise DateInputError(Message[arg+'_not_number'].value)
    else:
        if 'start' in arg:
            month = 1
        else:
            month = 12

    return month
