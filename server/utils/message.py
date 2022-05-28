class Message():
    """class to messages of return"""
    start_year_not_number = "start_year Not Is Number!"
    start_year_future = "start_year Is Future!"

    end_year_not_number = "end_year Not Is Number!"
    end_year_furure = "end_year Is Future!"

    start_month_not_number = "start_month Not Is Number!"
    end_month_not_number = "end_month Not Is Number!"

    def __init__(self, value):
        self.value = getattr(Message, value)


if __name__ == '__main__':
    print(Message('start_year_not_number').value)
    print(Message('start_year_future').value)

    print(Message('end_year_not_number').value)
    print(Message('end_year_furure').value)
