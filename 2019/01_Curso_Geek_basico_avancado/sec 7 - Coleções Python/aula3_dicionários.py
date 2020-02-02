"""

Em algumas linguagens, Dicionários = Mapas

Dicionário = {}
Lista = []
Tuplas = ()

Cada valor vai ter sua chave no Dicionário

exemplo: paises = {'chave':'valor',....}
exemplo não usual (eu gostei) -> paises = dict(chave1=valor1,chave2=valor2...)

Ou seja, nas listas e tuplas a chave já vem nos elementos,
exemplo x = ['oi','tchau'].... x [0] = 'oi' ...
perceba que o 0 é a chave do elemento 'oi' por
padrão... a chave está definida

OBS: Não podemos ter chaves iguais...
exemplo: x = {10:"ana, 10: 'miguel'}

"""


aluno = {'legal':'Ana','chato':'Miguel',10:'Priscila'}

#Chamando os Elementos pelas Chaves
print(aluno)
print(aluno['legal'])
print(aluno['chato'])
print(aluno[10])
#print(aluno['erro']) #Vai dar Erro! (KeyError)


#Forma mais apropriada - pois se você não tiver a chave, ele não dá
#erro como no exemplo acima, somente marca que é None
print(aluno.get('legal'))
print(aluno.get('chato'))
print(aluno.get(10))
print(aluno.get("erro")) # Esse ele não dá erro, retorna None


# Procurando uma chave dentro de um dicionário (Não procura elemento)

print("legal" in aluno)

if "chato" in aluno:
    print("ok")
else:
    print("Não")

# Localidades - Exemplo:

#OBs: PYTHON 3.7 não aceita 023.. (zero na frente)
local = {
    (123,230): "Brasil",
    (111,23): "Japão",
    (121,111): "USA"
}

print(local.get((123,230)))
print(local[(123,230)])

#Adicionando elementos a um dicionário

receita = {"jan":100, "fev": 150, "mar": 270}

receita["abr"] = 340 #add forma 1

receita.update({"mai": 500}) #add Forma 2 (Mais usada)

print(receita)

# Remover Elementos de um Dicionário

# Forma 1

print(receita.pop("jan")) # Retorna o Elemento

print(receita)

# Forma 2

del receita["mar"] # Não retorna o Elemento (não da para dar print)

print(receita)


# Exemplo de Produtos... por ------Tuplas------

"""
produto 1 = nome, quantidade, preço
produto 2 = ....

"""
q = int(input("Quantos você deseja?"))

produto1 = ("Playstation",q,q*23000)
print(produto1)



k = int(input("Quantos você deseja?"))

produto2 = ("Shampoo",k,k*20)
print(produto2)

# Exemplo de Produtos por -------DICIONÁRIO------

produto3 = {"Nome":"PlayStation",
            "Quantidade": 1,
            "Preço": 2000
}

#print("\n"+str(produto3["Preço"]))

produto4 = {"Nome":"Notebook",
            "Quantidade": 1,
            "Preço": 800
}

carrinho = []

carrinho.append(produto3)
carrinho.append(produto4)

print(carrinho)

#Forma não usual de criar Dicionário

c = dict(nome="playstation", quantidade= "1", valor = "2300")

print(c)

#Limpar um Dicionário

c.clear()

print(c)

# Deep Copy e Shallow Copy (Mesma coisa nas listas)]

#Deep Copy
a = {1:1,2:2}

b = a.copy()

b["oi"] = 10 # ou ...
b.update({'tchau':10})

print(b)

#Shallow Copy

h = b

b.pop("oi")

print(h)
print(b)

# Mudou 1... Mudou o outro...

#Fazer Várias Chaves e Valores: FromKeys(Sequencias...)

# {}.fromkeys(VARIA, CONSTANTE)

g = {}.fromkeys(range(0,10),"teste")

print(g)

# exemplo diferente - quero variar a chave e o elemnto

m ={}

p = ("cachorro","gato","aranha")
q = ("4 patas", "4 patas","8 patas")

for i in range(0,len(p)):

    m.update({p[i]:q[i]})

print(m)

