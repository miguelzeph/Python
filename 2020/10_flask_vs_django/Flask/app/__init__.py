from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager # Permite executar as funções do script diretamente pelo TERMINAL
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config.from_object('config') # Não usar extencao .py no config

db = SQLAlchemy(app)

migrate = Migrate(app,db) # Conecta flask e db

manager = Manager(app)
manager.add_command('db',MigrateCommand)

# Importar aqui, pois necessitamos dos comandos acima no arquivo default.py
from app.controllers import default
