from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def aula_01():
    message = 'Hello Flask'
    return render_template('aula_01.html', message = message)

@app.route('/02')
def aula_02():
    message = 'Hello Flask'
    return render_template('aula_02.html', message = message)

@app.route('/03')
def aula_03():
    message = 'Hello Flask'
    return render_template('aula_03.html', message = message)

if __name__ == '__main__':
    app.run(debug=True)