class DateInputError(Exception):
    ...

class EnvIndexIsNotAJson(Exception):
    ...

class IndexDateError(Exception):
    def __init__(self) -> None:
        super().__init__('Date Invalid Type Error!')
