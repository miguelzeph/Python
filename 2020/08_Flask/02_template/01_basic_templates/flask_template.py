from flask import (
	Flask,
	render_template
	)

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('basic.html')# O arquivo tem que estar na pasta TEMPLATES

if __name__ == '__main__':
	app.run()