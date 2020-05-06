from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    BooleanField,
    DateTimeField,
    RadioField,
    SelectField,
    TextField,
    TextAreaField,
    SubmitField
    ) 
from wtforms.validators import DataRequired

class InfoForm(FlaskForm):
    nome = StringField(
        "Qual o seu nome?",
        validators = [DataRequired()]
        )
    sexo = RadioField(
        'Qual o seu sexo: ',
        choices = [('M','Masculino'),('F','Feminino')]
        )
    cor = SelectField(
        'Selecione sua cor: ',
        choices = [('b', 'Branco'),('a','Amarelo'),('n','Negro')]
        )
    feedback = TextAreaField('Informações adicionais: ')
    termo = BooleanField('Aceita os termos?')
    submit = SubmitField('ENVIAR')

class SimpleForm(FlaskForm):
    submit = SubmitField("Salvar Dados")