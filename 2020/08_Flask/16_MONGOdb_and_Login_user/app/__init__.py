# Constructor and Config
from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

#################MONGODB######################
# MongoDB Config (Cadastrar no www.mlab.com)
app.config['MONGO_URI'] = 'mongodb+srv://admin:admin@cluster0.7rvyr.mongodb.net/teste?retryWrites=true&w=majority'
# Create Object MongoDB
mongo = PyMongo(app)
##############################################