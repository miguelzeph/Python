import os

# Pegar o nome do Dir atual que se encontra config.py
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(basedir, 'banco.db')
# Para poder rastrear as modificações no banco de dados
SQLALCHEMY_TRACK_MODIFICATIONS = True 
