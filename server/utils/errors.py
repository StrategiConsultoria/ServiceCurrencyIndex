class DateInputError(Exception):
    def __init__(self, error):
        super().__init__(error)


class IndexNameError(Exception):
    def __init__(self):
        super().__init__('Name Indice Invalid ["ipca","incc","igpm"]!')


class IndexDateError(Exception):
    def __init__(self):
        super().__init__('Date Invalid Type Error!')
