from flask import request, current_app, jsonify, send_file, abort
from server.database.indices import Indice
from server.utils.controlers import update_database
from server.utils.message import Message
from datetime import datetime
import pandas
import json
import tempfile

app = current_app


def init_app(app):
    app.init_app(app)


@app.route('/<file>/')
async def all_indices(file):
    if not file in ('json', 'csv'):
        abort(404)

    indice = request.args.get('indice')
    if indice:
        await update_database()

        items = await Indice.filter(name=indice).order_by('date').all()
        data_indice = []
        for item in items:
            data_indice.append(item.to_json())
        
        df = pandas.DataFrame(data_indice)


        if file == 'csv':
            file_temp = tempfile.NamedTemporaryFile()
            df.to_csv(file_temp.name, encoding='utf-8', index=False)
            return send_file(file_temp.name, download_name=f'{indice}.csv')
        else:
            return json.loads(df.to_json())

    else:
        await update_database()

        items = await Indice.all().order_by('date').all()
        data_indice = {
            "ipca": [],
            "incc": [],
            "igpm": []
        }
        for item in items:
            if item.name == 'ipca':
                data_indice['ipca'].append(item.to_json())
            elif item.name == 'incc':
                data_indice['incc'].append(item.to_json())
            elif item.name == 'igpm':
                data_indice['igpm'].append(item.to_json())

        df = pandas.DataFrame(data_indice)

        if file == 'csv':
            file_temp = tempfile.NamedTemporaryFile()
            
            df.to_csv(file_temp.name, encoding='utf-8', index=False, sep=';')
            return send_file(file_temp.name, download_name='data.csv')

        else:
            return json.loads(df.to_json())


@app.route('/<file>/<year>/')
async def filter_year(file, year):
    date_now = datetime.now()
    
    indice = request.args.get('indice')

    try: # verifi year if error return
        year = int(year)
        if not year >= 1 and not year <= date_now.year:
            return Message.year_invalid_is_future
    except:
        return Message.year_invalid_not_is_number

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

    try: # verifi end_year if not defined set year
        end_year = request.args.get('end_year', None)
        if end_year:
            end_year = int(end_year)
            if not year >= 1 and not year <= date_now.year:
                return Message.end_year_invalid_is_future
        else:
            end_year = year
    except:
        return Message.end_year_invalid_not_is_number


    if indice: # filter indice
        await update_database()
        
        data_indice = []

        items = await Indice.filter(name=indice, date__range=[f'{year}-{start_month}', f'{end_year}-{end_month}']).order_by('date') # filter indice range date values
        for item in items:
            data_indice.append(item.to_json()) # add item in data how json
        
        df = pandas.DataFrame(data_indice)

        if file == 'csv':
            file_temp = tempfile.NamedTemporaryFile()
            
            df.to_csv(file_temp.name, encoding='utf-8', index=False, sep=';')
            return send_file(file_temp.name, download_name=f'{indice}_{start_month}-{year}_{end_month}-{end_year}.csv')

        else:
            return json.loads(df.to_json())

    else:
        await update_database()

        data_indice = {"ipca": [], "incc": [], "igpm": []}
        
        items = await Indice.filter(date__range=[f'{year}-{start_month}', f'{end_year}-{end_month}']).order_by('date') # filter indice range date values
        for item in items:
            if item.name == 'ipca':
                data_indice['ipca'].append(item.to_json())
            elif item.name == 'incc':
                data_indice['incc'].append(item.to_json())
            elif item.name == 'igpm':
                data_indice['igpm'].append(item.to_json())

        df = pandas.DataFrame(data_indice)
        return json.loads(df.to_json())
