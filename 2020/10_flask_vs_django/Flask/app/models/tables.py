from app import db # importar do arquivo construtor (__init__) vc pode pegar variável direto 

class Pessoa(db.Model):

    # Criar Tabela
    __tablename__ = 'pessoas'

    # Criar Colunas
    id = db.Column(db.Integer, primary_key = True) # Gerado de forma AUTOMÁTICA
    nome = db.Column(db.String(50),nullabel= False) # 50 caracteres, nullabel = False indica que não pode ficar vazio
    idade = db.Column(db.Integer)
    sexo = db.Column(db.String(1))
    salario = db.Column(db.Float)

    #Construtor para classe
    def __init__(self,nome = 'Anônimo',idade =18,sexo = "M",salario=1039):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.salario = salario
    
    def __repr__(self):
        return "<Pessoa %r>" % self.nome


