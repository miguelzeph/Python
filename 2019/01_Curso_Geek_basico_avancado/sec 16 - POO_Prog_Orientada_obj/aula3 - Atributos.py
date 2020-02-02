"""
Atributos = Representam as características do Objeto

Em python, temos 3 atributos:
 - Atributos de Instância
 - Atributos de Classe
 - Atributos Dinâmico


#Em Java, uma classe lâmpada ficaria...

public class Lampada(){
    private int voltagem;
    private String cor;
    private Boolean ligada = false;

    public Lampada(int voltagem, String cor){
        this.voltagem = voltagem;
        this.cor = cor;
    }
}

"""

#Vamos fazer o em Python ( Atributos PÚBLICOS)


class Lampada:

    def __init__(selfself,voltagem,cor):

        # O Private do Java, no Python é
        # o duplo UNDERLINE
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False
        #Privado, só dentro da classe tenho
        #Acesso...

#OBS: Self = objeto que está executando
# o método...(Não é obrigado usar SELF como nome...)

class ContaCorrente:

    #Função dentro de Calsse = MÉTODO
    def __init__(self, numero, limite,saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo



class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
#----- Podemos trocar o nome de Self ---
class Teste:
    #Não é recomendado trocar o nome SELF
    #mas funciona sim...
    def __init__(cerveja,nome,idade):
        cerveja.nome = nome
        cerveja.idade = idade
#---------------------------------------




#Atributos Públicos e Atributos Privados

#Privado = __nome (tem que ter os 2 underline)
#obs: em java vc usa o "private"


# em python, por convenção, ficu estabe-
#lecido que todo atributo de uma classe
# será PÚBLICOOOOO


class Acesso:

    def __init__(self, email, senha):
        self.email = email #Público
        self.__senha = senha #Privado

    def mostra_senha(self):

        print(self.__senha)

    def mostra_email(self):
        print(self.email)
#OBS: você pode acessar atributos privados
#fora da classe... veja os exemplos

user = Acesso('user@gmail.com','1234')

print(user.email) #Público
#print(user.__senha) #Privado, forma errada


#print(dir(user)) #Ata, vi que o PRivado, tem que chamar "_Classe__atributo"

#Fazendo Acesso ao Atributo Privado
#fora da Classe...


# Isso é um Name Mangling
print(user._Acesso__senha) # Temos Acesso, mas não deveriamos ter acesso a ela...

#Fazendo Acesso ao Atributo Privado
#dentro da pŕopia classe

user.mostra_senha() #Forma melhor

# Viu a diferença de fazer acesso ao
#Atributo privado DENTRO e FORA da
#Própria Classe...

# O Público também pode ser acessado
#assim...

user.mostra_email()

print('\n')

# Atributos de Instância ------

# Significa, que ao criarmos instâncias de uma classe, todas as instâncias terão estes atributos...


user1 = Acesso('teste@gmail.com','123')
user2 = Acesso('teste2@gmail.com','123')


# Atributos de Classes (Atributos Estáticos) --------------

class Produto:

    #Isso são Atributo de Classe...(EM JAVA SÃO CHAMADOS DE "ATRIBUTOS ESTÁTICOS"
    imposto = 1.05 #0.05 de imposto
    contador = 0

    def __init__(self, nome, descricao,valor):
        self.id = Produto.contador+1 #Legal...
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor*Produto.imposto)
        Produto.contador = self.id #Legal ...

p1 = Produto("abc","game",1500)

print(p1.imposto)
print(p1.valor)

print(Produto.imposto) # Forma correta de acessar o  ATRIBUTO DE CLASSE


p2 = Produto("abcd","game",1500)
p3 = Produto("xbox","game",2500)
p4 = Produto("ps1","game",3000)

print(f"id(s): {p1.id} {p2.id} {p3.id} {p4.id}")

#------Atributos Dinâmicos (NÃO É COMUM USAR ...)-----------

# Você coloca fora da classe, veja...

p1.peso = '10kg' #Veja que não temos esse Atributo "peso"

print(p1.peso)


print('\n\n')

# -------- Deletando Atributos ----------

print(p1.__dict__)
print(p2.__dict__)

del p1.peso
del p2.nome

print('\n')

print(p1.__dict__)
print(p2.__dict__)

