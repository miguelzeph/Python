from flask import Flask, render_template, request, redirect, url_for
import stripe

app = Flask(__name__)

public_key = "pk_test_6pRNASCoBOKtIshFeQd4XMUh"
stripe.api_key = "sk_test_BQokikJOvBiI2HlWgH4olfQ2"


#FONTE: https://github.com/tylim88/Flask-Bootcamp-master/tree/master/10-Accepting-Payments-with-Flask/00-Payments


@app.route('/')
def index():
    return render_template('index.html',public_key= public_key)

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

@app.route('/payment',methods = ['POST'])
def payment():

    # Customer Info
    customer = stripe.Customer.create(
        email=request.form['stripeEmail'],
        source = request.form['stripeToken']
    )

    # Payment Information
    charge = stripe.Charge.create(
        customer = customer.id,
        amount = 1999,
        currency = 'usd',
        description = 'Donation'
    )

    return redirect(url_for('thankyou'))

if __name__ == '__main__':
    app.run(debug=True)