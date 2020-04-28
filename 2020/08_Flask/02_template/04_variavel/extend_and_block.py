from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('basic.html')

@app.route('/home/<name>')
def home(name):
	return render_template("home.html",name = name)

if __name__ == '__main__':
	app.run(debug = True)