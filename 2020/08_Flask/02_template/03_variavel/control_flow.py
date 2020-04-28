from flask import (
	Flask,
	render_template
	)

app = Flask(__name__)


# Acessando variáveis---------------
#No HTML você acessa o python com o Jinja {{}}
@app.route('/')
def index():

	mylist = [0,1,2,3,4]
	letras = ['a','b','c','d','e']

	return render_template(
		'basic.html',
		mylist = mylist,
		myletras= letras,
		)
#-------------------------------------

if __name__ == '__main__':
	app.run(debug = True)