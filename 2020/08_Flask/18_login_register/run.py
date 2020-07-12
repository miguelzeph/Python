from flask import Flask, session, request, url_for, redirect, render_template, flash
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb+srv://useradmin:admin@cluster0.7rvyr.gcp.mongodb.net/TESTE_LOGIN?retryWrites=true&w=majority"
app.config['SECRET_KEY'] = 'mysecretkey'
mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registrar')
def registrar():
    return render_template('registrar.html')

@app.route('/criar', methods = ['POST','GET'])
def criar():
    if request.method == 'POST':
        usuario = mongo.db.usuario
        add = {}
        for parametro in request.form:
            add[str(parametro)] = request.form[str(parametro)]
        
        
        if usuario.find_one({'nome':add['nome']}) is None:
            if add['senha'] == add['senha_confirmar']:
                
                imagem = request.files['imagem']
                mongo.save_file(imagem.filename,imagem)
                add['imagem'] = imagem.filename

                # Salvar informações
                usuario.insert(add)
                
            else:
                flash('Confirmação de senha inválida','danger')
                return redirect(url_for('registrar'))   
            
        else:
            flash('Já existe este usuário','danger')
            return redirect(url_for('registrar'))

    return redirect(url_for('index'))

@app.route('/login')
def login():
    return ''
@app.route('/logout')
def logout():
    #session.clear()
    return ''



if __name__ == '__main__':
    app.run(debug=True)