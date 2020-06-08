from flask import (
    render_template,# renderiza template
    request # captura dados recebido por formulários
    )
from app import app, db # Estamos importando do CONSTRUTOR __init__
from app.models.tables import Pessoa

@app.route('/')# Rota
@app.route('/listagem')# Rota
def listagem():
    pessoas = Pessoa.query.all()

    return render_template(
        'listagem.html',
        pessoas = pessoas,
        ordem = 'id'
    )

@app.route('/selecao/<int:id>')# Rota
def selecao(id=0):# Coloquei id default =0, caso não seja definido na URL (esqueça)
    pessoa = Pessoa.query.filter_by(id=id).all()

    return render_template(
        'listagem.html',
        pessoas = pessoa,
        ordem = 'id'
    )

@app.route('/ordenacao/<campo>/<ordem_anterior>')
def ordenacao(campo='id',ordem_anterior=''):
    if campo == 'id':
        if ordem_anterior == campo:
            pessoas = Pessoa.query.order_by(Pessoa.id.desc()).all()# Ordem decrescente
        else:
            pessoas = Pessoa.query.order_by(Pessoa.id).all()# Ordem decrescente

    elif campo == 'nome':
        if ordem_anterior == campo:
            pessoas = Pessoa.query.order_by(Pessoa.nome.desc()).all()# Ordem decrescente
        else:
            pessoas = Pessoa.query.order_by(Pessoa.nome).all()# Ordem decrescente

    elif campo == 'idade':
        if ordem_anterior == campo:
            pessoas = Pessoa.query.order_by(Pessoa.idade.desc()).all()# Ordem decrescente
        else:
            pessoas = Pessoa.query.order_by(Pessoa.idade).all()# Ordem decrescente

    elif campo == 'sexo':
        if ordem_anterior == campo:
            pessoas = Pessoa.query.order_by(Pessoa.sexo.desc()).all()# Ordem decrescente
        else:
            pessoas = Pessoa.query.order_by(Pessoa.sexo).all()# Ordem decrescente
    
    elif campo == 'salario':
        if ordem_anterior == campo:
            pessoas = Pessoa.query.order_by(Pessoa.salario.desc()).all()# Ordem decrescente
        else:
            pessoas = Pessoa.query.order_by(Pessoa.salario).all()# Ordem decrescente

    else:
        pessoas = Pessoa.query.order_by(Pessoa.id).all()# Ordem decrescente

    return render_template(
        'listagem.html',
         pessoas = pessoas,
         ordem = campo
    )


@app.route('/consulta', methods = ['POST'])
def consulta():
    consulta = '%'+request.form.get('consulta')+'%'
    campo = request.form.get('campo')
    
    if campo == 'nome':
        pessoas = Pessoas.query.filter(Pessoa.nome.like(consulta)).all
    elif campo == 'idade':
        