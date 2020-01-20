"""
Modulo Collection Default Dict - serve para pessoas que buscam valores por chaves erradas dentro dos
dicionários


OBS: LAMBDA = são funções sem nome, que podem ou não receber valores de entrada e reotrnarem valores


"""

from collections import defaultdict

dicionario = defaultdict(lambda: 9999999) #criamos um Dicionário

print(dicionario) #Vazio

dicionario["oi"] = "tchau" #add a chave: elemento ao dicionario

print(dicionario)

print(dicionario["valor_que_nao_tem"]) # antes dava KeyError quando você digitava um valor que não tinha
#dentro do dicionário... Agora além de não dar erro, ele retorna o valor do lambda 99999 ....

print(dicionario) # Além disso, ele adiciona uma chave nova com o valor procurado ("valor_que_nao_tem)
#e joga nela o valor do lambda que você escolheu (999999)

