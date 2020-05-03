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
def index():
    return render_template('./index.html')
    
@app.route('/calculado')
def calcular():
    temperatura =request.args.get("temperatura")

    try:
        resultado = model.predict([[float(temperatura)]])
        resultado = round(resultado[0][0],2)
        print('###################################################\n')
        print(f'{temperatura}°Celsius ===> {resultado}°Fahrenheits')
        print('###################################################\n')

        return render_template(
            './resultado.html',
            temp =temperatura,
            res = resultado,
            )
    #Coloquei um valor que não seja ńumero, logo o modelo não faz predições       
    except:
        return render_template('error.html',temp = temperatura)

if __name__ == '__main__':
    port = int(os.environ.get('PORT',5500))
    app.run(host='0.0.0.0',port = port,debug = True)