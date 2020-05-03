from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup_form')
def signup_form():
    return render_template('signup.html')

@app.route('/thankyou')
def thank_you():
    first = request.args.get('first') # "name' que vc coloca no html
    last = request.args.get('last') # "name' que vc coloca no html
    return render_template(
        'thankyou.html',
        first = first, #Envia o First para o html
         last= last    #Envia o Last para o html
          )

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug = True)