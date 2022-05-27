class Message():
    """class to messages of return"""
    start_year_invalid_not_is_number = {"Error": "Year not is number"}
    start_year_invalid_is_future = {"Error": "Year invalid is future"}

    

    end_year_invalid_is_future = {"Error": "End year invalid is future"}
    end_year_invalid_not_is_number = {"Error": "End year not is number"}

    start_month_invalid_not_in_interval = {
        "Error": "Start month invalid not in invalid 1 - 12"}
    start_menth_invalid_not_in_number = {"Error": "Start month not is number"}

    end_month_invalid_not_in_interval = {
        "Error": "End month invalid not in invalid 1 - 12"}
    end_month_invalid_not_in_number = {"Error": "End month not is number"}
