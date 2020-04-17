from flask import (
	Flask,
	render_template
	)

app = Flask(__name__)

@app.route('/')
def index():

	some_variable = 'Priscila'
	meu_nome = 'Miguel'
	dictionary = {
		'Produto':'Computador',
		'Preço': 500,
		'Ano': 2018
		}

	return render_template(
		'basic.html',
		my_variable = some_variable,
		outra_variavel = meu_nome,
		my_dict = dictionary
		)

if __name__ == '__main__':
	app.run(debug = True)