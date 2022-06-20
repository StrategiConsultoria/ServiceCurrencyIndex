class NAN(Exception):
    def __init__(self, value):
        super().__init__(f'{value} - is not a number!')
