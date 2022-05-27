class DateInputError(Exception):
    def __init__(self):
        super().__init__('Date Invalid year.month')


class IndiceNameError(Exception):
    def __init__(self):
        super().__init__('Name Indice Invalid ["ipca","incc","igpm"]!')


class IndiceDataError(Exception):
    def __init__(self):
        super().__init__('Date Invalid Type Error!')
