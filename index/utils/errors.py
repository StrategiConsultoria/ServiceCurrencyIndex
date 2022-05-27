class SeridNotInformedError(Exception):
    def __init__(self):
        super().__init__('serid not informed!')

class SeridNotIsNumberError(Exception):
    def __init__(self):
        super().__init__('serid informed not is number')