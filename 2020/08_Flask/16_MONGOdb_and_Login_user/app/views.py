from app import app, mongo
from flask import request, render_template, session,redirect,url_for, flash
import bcrypt

@app.route('/')
def index():

    #session.clear()
    log = False
    if 'logado' in session:
        log = True
    
    return render_template('index.html', log = log)


@app.route('/register', methods=['POST','GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name':request.form['username']})
        if existing_user is None: # Se não existir, cadastre
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'),bcrypt.gensalt())
            users.insert({'name':request.form['username'],'password':hashpass})
            #session['username'] = request.form['username']
            flash('Nome Registrado com Sucesso','success')
            return redirect(url_for('index'))
        flash('Nome já Registrado','danger')
    return render_template('register.html')

@app.route('/login', methods=['POST',"GET"])
def login():
    if request.method == "POST":
        users = mongo.db.users
        login_user = users.find_one({'name': request.form['username']})

        if login_user:
            if bcrypt.hashpw(request.form['password'].encode('utf-8'), login_user['password']) == login_user['password']:
                session['logado'] = True
                flash(f' Usuário {request.form["username"]} Logado','success')
                return redirect(url_for('index'))
        flash('Usuário ou senha inválida','danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))
    
    