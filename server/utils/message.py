from enum import Enum


class Message(Enum):
    """class to messages of return"""
    start_year_not_number = "start_year Is Not a Number!"
    start_year_future = "start_year Is Future!"

    end_year_not_number = "end_year Is Not a Number!"
    end_year_furure = "end_year Is Future!"

    start_month_not_number = "start_month Is Not a Number!"
    end_month_not_number = "end_month Is Not a Number!"

class MessageLog(Enum):
    """class to message of log"""
    env_index_not_found = '.env -> INDEXS Not Found' 
    env_index_not_json = 'INDEXS Is Not a Json' 

    date_invalide_new_index = 'Date Invalid In Create Index'