import tempfile
from datetime import datetime
from datetime import date as dt

from flask import current_app,request,jsonify,send_file
import pandas

from server.database.models.index import Index
from server.utils.capture import get_date_in_args


app = current_app

@app.route('/api/<file>')
def ipeadata_route(file):
    index_name = request.args.get('index')
    if not index_name:
        return jsonify({'error':'arg index is not a found'}),402
    if not file in ('json','csv'):
        return jsonify({'error':'file json or csv'}),402
    date_now = datetime.now()

    try:
        start_year = get_date_in_args('start_year',1000,1000,date_now.year)
        end_year = get_date_in_args('end_year',date_now.year,1000,date_now.year)
        start_month = get_date_in_args('start_month',1,1,12)
        end_month = get_date_in_args('end_month',12,1,12)
    except Exception as error:
        return jsonify({'error':str(error)}),402

    try:
        decimal = int(request.args.get('decimal',6))
    except:
        decimal = 6
    

    start_date = dt(start_year,start_month,1)
    end_date = dt(end_year,end_month,1)

    index_name = index_name.upper()
    indexs = Index.query.filter_by(NAME=index_name).filter(Index.DATE.between(start_date,end_date)).order_by(Index.DATE.desc()).all()
    if file == 'json':
        response = {}

        for index in indexs:
            response[index.date] = format_money(index.index,decimal)
        return jsonify(response)   
    else:
        file_temp = tempfile.NamedTemporaryFile()
        response = [{'DATE':index.date,'INDEX':format_money(index.index,decimal)} for index in indexs]
        df = pandas.DataFrame(response)
        df.to_csv(file_temp.name, encoding='utf-8', index=False, sep=';')
        return send_file(file_temp.name, download_name=f'{index_name}_{start_month}-{start_year}_{end_month}-{end_year}.csv')

def format_money(value,decimal):
    formato = '{:.'+str(decimal)+'f}'
    return formato.format(value).replace('.',',')
    
    
    




