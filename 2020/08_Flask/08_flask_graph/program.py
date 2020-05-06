from flask import Flask, render_template
import matplotlib.pyplot as plt
import numpy as np
import os

app = Flask(__name__)

local = os.getcwd()

@app.route('/')
def index():
    
    return render_template('index.html')

#DICA: SHIFT+CTRL+R para atualizar a página deletando os cache
@app.route('/graph_plot')
def graph():
    x = np.arange(0,10)
    y = -x
    plt.plot(x,y)
    url = './static/image/graf.png'
    plt.savefig(url)
    plt.close()
    return render_template(
        'graf.html',
        url = url,
        name = 'grafico Novo',
        )

if __name__ == '__main__':
    app.run(debug = True)