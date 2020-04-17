from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return '<h1>Hello World!</h1>'

@app.route('/information')
def info():
	return '<h1>Obtenha informações</h1>'

@app.route('/puppy/<name>')
def puppy(name):
	return f"<h1>This is a page for {name.upper()}</h1>"

@app.route('/tamanho/<teste>')
def tamanho(teste):
	return f'<h1> Printa a letra de índice 5 {teste[5]}</h1>'

#--------------------Exercise---------------------------
from flask import request

@app.route('/puppy_name/<name>')
def puppylatin(name):
	pupname = ''
	if name[-1] == 'y':
		pupname = name[:-1] + 'iful'
	else:
		pupname = name+'y'
	return f"<h1> Your puppy latin name is: {pupname}"
#-------------------------------------------------------

if __name__ == '__main__':
	app.run(debug = True)# Deixar como False quando for para a produção!



