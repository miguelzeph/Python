"""
Métodos Mágicos = tudo que é do python e tem o __xxx__ (fica roxinho no pycharm)

Exemplo:

__init__ = Método construtor

__repr__ = Representação de Objetos

__len__ = igual ao len()... mas versão para classe

__del__ = quando você deletar, irá fazer  o que vc mandou

__add__ = + (soma)

... veja todos... ---> dir(object)

#... De onde vem esses métodos Mágicos??? do nosso "object" (de baixo dos panos)
"""

class Livro(object): #Vem tudo daqui... os métodos mágicos

    def __init__(self, titulo, autor, paginas):

        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __repr__(self): #Fazer representação
        return self.titulo

    def __str__(self): #Representação também.
        return self.autor
    #OBS: __str__ > __repr__ ... Se tiver os dois, ele executa o __str__ (Caso eu use o Print direto)

    def __len__(self):
        #return len(self.titulo)
        #return len(self.autor)
        return self.paginas

    def __del__(self):
        print('Você deletou algo')

    def __add__(self, outro): # Soma de objetos +
        return f"{self} - {outro}"

    def __mul__(self, other): # utilizado para multiplciação *

        if isinstance(other, int): #Estou chegando se é um inteiro...
            msg = ''
            for n in range(other):
                msg += ' '+str(self)
            return msg
        return "Não posso multiplicar"

livro1 = Livro('Python para iniciantes', "Inpe", 200)
livro2 = Livro('Teste','Unitau',300)

print(livro1)# __str__ > __repr__... se eu usar o print direto

#Agora eu posso escolher.
print(repr(livro1))
print(str(livro1))

print(len(livro1))

#del(livro1)

print(livro1 + livro2) # usa o __add__

print(livro1*3)

# Após o Python usar os objetos, ele deleta no final do programa

