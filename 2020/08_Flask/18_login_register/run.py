from flask import Flask, session, request, url_for, redirect, render_template, flash
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb+srv://useradmin:admin@cluster0.7rvyr.gcp.mongodb.net/TESTE_LOGIN?retryWrites=true&w=majority"
app.config['SECRET_KEY'] = 'mysecretkey'
mongo = PyMongo(app)

@app.route('/')
def index():
    log = False
    if 'log' in session:
        log = True
    return render_template('index.html', log = log)

@app.route('/registrar')
def registrar():
    return render_template('registrar.html')

@app.route('/criar', methods = ['POST','GET'])
def criar():
    if request.method == 'POST':
        usuario = mongo.db.usuario # Cria uma Tabela "usuario" dentro do #TESTE_LOGIN
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

    return redirect(url_for('login'))

@app.route('/login', methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        
        usuario = mongo.db.usuario
        if usuario.find_one({'nome':request.form['nome']}) is None:
            flash('Usuário não cadastrado','danger')
        else:
            usuario_nome = usuario.find_one({'nome':request.form['nome']})
            
            if usuario_nome['senha'] == request.form['senha']:
                session['log'] = True
                flash('LOGADO','danger')
                return redirect(url_for('index'))
            else:
                
                flash('Senha Incorreta','danger') 
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    #session.clear() # Remove tudo
    session.pop('log') # Remove um
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)