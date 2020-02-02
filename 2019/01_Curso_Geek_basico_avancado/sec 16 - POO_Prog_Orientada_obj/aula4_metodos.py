"""
Métodos = funções dentro de classes

Em python, são divididos em: Método de Instância e Método de Classe


O método dunder __init__ é um método especial, chamado de CONSTRUTOR...
ele constroi o OBJETO a partir da classe.

OBS: Todo elemento com 2 underline antes e depois = Dunder

OBS: Os métodos Dunder em Python são chamados de Métodos Mágicos
(Método Mágico = Fica ROXO)

OBS: Por mais que possamos criar nossas próprias funções com DUNDER, isso não é
Aconselhavel! Evite, pois os Dunder são métodos internos do próprio Python




"""

class Lampada:

    def __init__(self, cor, voltagem, luminosidade):

        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade

class ContaCorrente:

    contador = 4999

    def __init__(self, numero, limite, saldo):

        self.__numero = ContaCorrente.contador +1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero

class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):

        self.__id = Produto.contador +1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):

        """Retorna o valor do Produto com o Desconto"""
        return (self.__valor * (100 - porcentagem))/100

#Tem que instalar essa biblioteca de cripitografia
from passlib.hash import pbkdf2_sha256 as cryp



class Usuario:

    contador = 0

    #---------Método de Classe..-------------------
    @classmethod
    def conta_usuarios(cls): # cls = propria classe
        print(f'Temos {cls.contador} usuario(s) no sistema')
    #-----------------------------------------------


    #---------- Método Estático---------
    @staticmethod
    def definicao(): #não recebe nada
        return 'UXR344'

    def __init__(self, nome, sobrenome, email, senha):

        self.__id = Usuario.contador+1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        #Rounds = embaralhar x vezes, salt_size = tamanho do texto
        #self.__senha = cryp.encrypt(senha, rounds=200, salt_size=6) # A biblioteca pediu para usar o .hash()
        self.__senha = cryp.hash(senha, rounds = 200, salt_size = 6)
        Usuario.contador = self.__id
        print(f'Usuario criado: {self.__gera_usuario()}')


    #----------Métodos de Instância Público---------------------
    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def senha(self):
        return self.__senha

    def checa_senha(self, senha):

        if cryp.verify(senha, self.__senha):
            return True

        return False
    #---------------------------------------------------



    #---------Método de Instância Privado (__x)---------
    #Só acesso dentro da própria classe
    def __gera_usuario(self):
        return self.__email.split('@')[0]

"""

# ----------------MÉTODOS DE INSTÂNCIA ---------------------

#Criar Produto
p1 = Produto("Tv", "Video", 2300)


#Mais Recomendado
print(p1.desconto(50))

#Ou poderia fazer
#print(Produto.desconto(p1,50)) # self = meu objeto



print('\n')

#Criar Usuário

user1 = Usuario('Miguel','Amaral','miguel.junior@gmail.com','123456')

print(user1.nome_completo())


#Acesso de forma errado a um atributo Privado
print(f'Senha: {user1._Usuario__senha}')

#Forma correta (criar um método)
print(f'Senha: {user1.senha()}')

print('\n\n')

nome = input('Informe o nome: ')
sobrenome = input('Informe o sobrenome: ')
email = input('Informe o e-mail: ')
senha = input('Informe a senha: ')
confirma_senha = input('Confirme a senha: ')

if senha == confirma_senha:

    user = Usuario(nome, sobrenome,email,senha)

    print('Usuário criado com sucesso!')

else:

    print('Senha não confere...')

senha = input('informe a senha para acesso: ')

if user.checa_senha(senha):
    print('Acesso Permitido')
else:
    print('Acesso Negado')

"""

#--------------------Método de Classe-------------------------

user = Usuario("Miguel", 'Amaral', 'miguel@hotmail.com', '1234')

Usuario.conta_usuarios() #forma correta

user.conta_usuarios() # Incorreta


#----------Quando usar o Método de Classe e o de Instância????? --------

"""
A gente cria métodos de Instâncias, quando precisamos fazer acesso a Atributos de instâncias...

Métodos de classe (métodos estáticos EM OUTRAS LINGUAGENS) não acessa atributos de instância...

obs: Veja nos código... vc vai ver a diferença

"""



# Temos Também os Métodos PRIVADOS, que só podem ser acessados dentro da classe
#Utiliza-se duplo underline antes do nome da função!!!

user3 = Usuario('a','b','teste@gmail.com', '1234')

#print(user3.__gera_usuario()) # ERRO, ele é privado

print(user3._Usuario__gera_usuario()) #Acesso de forma Ruim


print('\n\n')


#------------Métodos Estáticos (Não varia)---------

# em python temos os métodos de Classe e Métodos Estáticos

print(Usuario.definicao())

