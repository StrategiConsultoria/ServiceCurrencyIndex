from flask import request


def get_date_in_args(arg,default,minimun,maximun) -> int:
    """ get numeric to date in args

    :entry:
        :arg: str -> Argument name
        :default: int -> Default number in case it doesn't exist
        :minimun: int -> Minimum number not to give date error
        :maximun: int -> Maximum number to not put future numbers
    
    :return:
        Exception
    
    :return:
        int
    
    """
    date = request.args.get(arg)
    if date:
        try:
            date = int(date)
            if date < minimun:
                date = minimun
            elif date > maximun:
                date = maximun

        except:
            raise Exception(f'{arg} - is not a number!')
    else:
        date = default
    return date