from flask import request, current_app, jsonify, send_file, abort
from server.database.indices import Indice
from server.utils.controlers import update_database
from server.utils.message import Message
from datetime import datetime
import pandas
import json
import tempfile
import logging

logging.info('Start Routes')
app = current_app


@app.route('/<file>')
async def index(file):
    date_now = datetime.now()
    
    indice = request.args.get('indice')

    try: # verifi start_month if not defined set 1 
        start_month = request.args.get('start_month', None)
        if start_month:
            start_month = int(start_month)
            if not start_month >= 1 and not start_month <= 12:
                return Message.start_month_invalid_not_in_interval
        else:
            start_month = 1
    except:
        return Message.start_menth_invalid_not_in_number

    try: # verifi end_month if not defined set 12 
        end_month = request.args.get('end_month', None)
        if end_month:
            end_month = int(end_month)
            if not end_month >= 1 and not end_month <= 12:
                return Message.end_month_invalid_not_in_interval
        else:
            end_month = 12
    except:
        return Message.end_month_invalid_not_in_number
    
    try: # verifi start_year if not defined set year
        start_year = request.args.get('start_year', None)
        if start_year:
            start_year = int(start_year)
            if not start_year >= 1 and not start_year <= date_now.year:
                return Message.start_year_invalid_is_future
        else:
            start_year = date_now.year
    except:
        return Message.start_year_invalid_not_is_number

    try: # verifi end_year if not defined set year
        end_year = request.args.get('end_year', None)
        if end_year:
            end_year = int(end_year)
            if not year >= 1 and not year <= date_now.year:
                return Message.end_year_invalid_is_future
        else:
            end_year = date_now.year
    except:
        return Message.end_year_invalid_not_is_number


    if indice: # filter indice
        
        data_indice = []

        items = await Indice.filter(name=indice, date__range=[f'{start_year}-{start_month}', f'{end_year}-{end_month}']).order_by('date') # filter indice range date values
        for item in items:
            data_indice.append(item.to_json()) # add item in data how json
        
        df = pandas.DataFrame(data_indice)

        if file == 'csv':
            file_temp = tempfile.NamedTemporaryFile()
            
            df.to_csv(file_temp.name, encoding='utf-8', index=False, sep=';')
            return send_file(file_temp.name, download_name=f'{indice}_{start_month}-{start_year}_{end_month}-{end_year}.csv')

        else:
            return json.loads(df.to_json())

    else:

        data_indice = {"ipca": [], "incc": [], "igpm": []}
        
        items = await Indice.filter(date__range=[f'{start_year}-{start_month}', f'{end_year}-{end_month}']).order_by('date') # filter indice range date values
        for item in items:
            if item.name == 'ipca':
                data_indice['ipca'].append(item.to_json())
            elif item.name == 'incc':
                data_indice['incc'].append(item.to_json())
            elif item.name == 'igpm':
                data_indice['igpm'].append(item.to_json())

        df = pandas.DataFrame(data_indice)
        return json.loads(df.to_json())
