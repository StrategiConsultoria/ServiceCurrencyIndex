from flask import request, current_app, jsonify, send_file, abort
from server.database.index import Index
from server.utils.controlers import update_database
from server.utils.message import Message
from server.utils.capture_requests import capture_month,capture_year
from server.utils.errors import DateInputError
from server.utils.responses import ResponseErrors
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
    
    index = request.args.get('index')

    try: # verifi start_month if not defined set 1 
        start_month = capture_month(request, 'start_month')
    except DateInputError as error:
        return ResponseErrors(str(error),request.args,request.form,request.method).value,400

    try: # verifi end_month if not defined set 12 
        end_month = capture_month(request, 'end_month')
    except DateInputError as error:
        return ResponseErrors(str(error),request.args,request.form,request.method).value,400

    try: # verifi start_year if not defined set year
        start_year = capture_year(request, 'start_year')
    except DateInputError as error:
        return ResponseErrors(str(error),request.args,request.form,request.method).value,400

    try: # verifi end_year if not defined set year
        end_year = capture_year(request, 'end_year')
    except DateInputError as error:
        return ResponseErrors(str(error),request.args,request.form,request.method).value,400
    

    if index: # filter indice
        
        items = await Index.filter(name=index, date__range=[f'{start_year}-{start_month}', f'{end_year}-{end_month}']).order_by('date') # filter indice range date values
        
        if file == 'csv':
            file_temp = tempfile.NamedTemporaryFile()
            data_indice = []
            for item in items:
                data_indice.append({'date':item.date.strftime('%d/%m/%Y'),'index':item.index.replace(',','.')})
            df = pandas.DataFrame(data_indice)
            df.to_csv(file_temp.name, encoding='utf-8', index=False, sep=';')
            return send_file(file_temp.name, download_name=f'{index}_{start_month}-{start_year}_{end_month}-{end_year}.csv')

        else:
            data_indice = {}
            for item in items:
                data_indice[item.date.strftime('%d/%m/%Y')] = item.index.replace(',','.')
            return jsonify(data_indice)

    else:

        data_indice = {"ipca": [], "incc": [], "igpm": []}
        
        items = await Index.filter(date__range=[f'{start_year}-{start_month}', f'{end_year}-{end_month}']).order_by('date') # filter indice range date values
        for item in items:
            if item.name == 'ipca':
                data_indice['ipca'].append(item.to_json())
            elif item.name == 'incc':
                data_indice['incc'].append(item.to_json())
            elif item.name == 'igpm':
                data_indice['igpm'].append(item.to_json())

        return jsonify(data_indice)
