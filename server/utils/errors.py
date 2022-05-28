class DateInputError(Exception):
    ...

class EnvIndexIsNotAJson(Exception):
    ...

class IndexNameError(Exception):
    def __init__(self) -> None:
        super().__init__('Name Indice Invalid ["ipca","incc","igpm"]!')


class IndexDateError(Exception):
    def __init__(self) -> None:
        super().__init__('Date Invalid Type Error!')
