from flask import request, current_app, jsonify, send_file, abort
from server.database.index import Index
from server.utils.controlers import update_database
from server.utils.message import Message
from server.utils.capture_requests import capture_month, capture_year
from server.utils.errors import DateInputError
from server.utils.responses import ResponseErrors
from datetime import datetime
import pandas
import json
import tempfile
import logging

logging.info('Start Routes')
app = current_app


@app.route('/<file>/')
async def index(file):
    date_now = datetime.now()

    index = request.args.get('index')

    try:  # verifi start_month if not defined set 1
        start_month = capture_month(request, 'start_month')
        end_month = capture_month(request, 'end_month')
        start_year = capture_year(request, 'start_year')
        end_year = capture_year(request, 'end_year')
    except DateInputError as error:
        return ResponseErrors(str(error), request).value, 400

    if index:  # filter indice

        # filter indice range date values
        items = await Index.filter(name=index, date__range=[f'{start_year}-{start_month}', f'{end_year}-{end_month}']).order_by('date')

        if file == 'csv':
            file_temp = tempfile.NamedTemporaryFile()
            data_index = []
            for item in items:
                data_index.append({'date': item.get_date_format, 'index': item.get_index_format})
            df = pandas.DataFrame(data_index)
            df.to_csv(file_temp.name, encoding='utf-8', index=False, sep=';')
            return send_file(file_temp.name, download_name=f'{index}_{start_month}-{start_year}_{end_month}-{end_year}.csv')

        else:
            data_index = {}
            for item in items:
                data_index[item.get_date_format] = item.get_index_format
            return jsonify(data_index)

    else:

        data_index = {}

        # filter indice range date values
        items = await Index.filter(date__range=[f'{start_year}-{start_month}', f'{end_year}-{end_month}']).order_by('date')
        for item in items:
            if data_index.get(item.name):
                data_index[item.name][item.get_date_format] = item.get_index_format
            else:
                data_index[item.name] = {item.get_date_format: item.get_index_format}

        return jsonify(data_index)
