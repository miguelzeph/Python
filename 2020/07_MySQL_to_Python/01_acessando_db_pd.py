import mysql.connector as sql
import pandas as pd


# Sabemos os nossos bancos de dados...
mydb = sql.connect(
    host = 'localhost',
    user = 'root',
    password = '25lokinho',
    database = 'cadastro',#vamos acessar
)


df = pd.read_sql('SELECT * FROM pessoas', con=mydb)

print(df)


