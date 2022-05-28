import os
import logging
import json
from .errors import EnvIndexIsNotAJson
from .message import MessageLog
def check_env():
    try:
        json.loads(os.environ['INDEXS'])
    except KeyError:
        logging.critical(MessageLog['env_index_not_found'].value)
    except:
        raise EnvIndexIsNotAJson(MessageLog['env_index_not_json'].value)


    
