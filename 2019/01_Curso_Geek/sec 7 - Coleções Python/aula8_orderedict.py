"""

Ordered Dict - ele faz com que a ordem influencie dentro de um dicionarios

"""

from collections import OrderedDict

dic1 = {"b":2, "a":1}
dic2 = {"a":1, "b":2}

print(dic1)
print(dic2)

print(dic1 == dic2) #True or False? resposta: True

#CONCLUIMOS QUE A ORDEM NÃO IMPORTA PARA OS DICIONÁRIOS... MESMO QUE SEJAM OS MESMOS
#VALORES

#Agora com o Dict

dic3 = OrderedDict({"b":2, "a":1})
dic4 = OrderedDict({"a":1, "b":2})

print(dic3 == dic4) # Resposta: False
# AGORA A ORDEM INTERFERE
