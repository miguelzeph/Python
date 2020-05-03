import numpy as np
import os
from flask import (
    Flask,
    request,
    render_template,
    make_response
    )
from sklearn.externals import joblib

app = Flask(__name__, static_url_path = '/static')
model = joblib.load('./modelo.pkl')


@app.route('/')
def display_gui():
    global temperatura
    temperatura = request.args.get('temperatura')

    return render_template('./template.html')
    

@app.route('/verificar')
def verificar():
    
    
    classe = model.predict([[float(temperatura)]])
    print(f'{temperatura} Celsius = {round(classe[0][0],2)} Fahrenheits')


    return render_template('./template.html')


if __name__ == '__main__':
    port = int(os.environ.get('PORT',5500))
    app.run(host='0.0.0.0',port = port)