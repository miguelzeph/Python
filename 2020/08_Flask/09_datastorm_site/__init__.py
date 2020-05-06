from flask import (
    Flask,
    render_template,
    redirect,
    session, # Quem faz as transferências de informações entre as funções
    url_for,
    flash
    )
from form import *
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'


#Dica: SHIFT+CTRL+R atualizar página deletando cache

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/serviço')
def service():
    return render_template('serviço.html')
    
@app.route('/cadastro/<user>',methods = ['GET','POST'])
def cadastro(user):
    
    form = InfoForm()  
    if form.validate_on_submit():
        session['nome'] = form.nome.data
        session['sexo'] = form.sexo.data
        session['cor'] = form.cor.data
        session['feedback'] = form.feedback.data
        session['termo'] = form.termo.data
        return redirect(url_for('thankyou',form = form))

    return  render_template(
        'cadastro.html',
        form=form,
        user = user
        )
@app.route('/thankyou',methods = ['POST','GET'])
def thankyou():
    form = SimpleForm()
    if form.validate_on_submit():
        arq = open('./cadastro.txt','w')
        escrever = f"Nome: {session['nome']}\nSexo: {session['sexo']}\nCor: {session['cor']}\nFeedback: {session['feedback']}\nTermo: {str(session['termo'])}\n"
        arq.write(escrever)
        arq.close()

        flash("Você salvou os dados")

    return render_template('thankyou.html',form = form)


if __name__ == '__main__':
    app.run(debug=True)