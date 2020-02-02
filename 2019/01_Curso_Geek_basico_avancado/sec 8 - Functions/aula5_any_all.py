"""
São bool (Booleanos)

All - retorna True se todos forem verdadeiros
any - retorna True se pelo menos um for verdadeiro


"""

#Exemplo 1

a = [0,1,2,3] # 0 = sempre False... resto é True

print(all(a)) # Falso
print(any(a)) # Verdadeiro, existe um elemento verdadeiro pelo menos

a.remove(0)

print(all(a)) # True... removeu o 0
print(any(a)) # True, só tem verdadeiros agora

print(all([])) # True - lista vazia
print(all([""])) # Falso
print(all([" "])) # True, espaço é verdadeiro

# Analisar os primeiros elementos, se todos começam com a letra C

nomes = ["Carla", "Camila", "Regina","carol","cintia"]

analise = all(nome[0].title() == "C" for nome in nomes) # title deixa a primeira Maiuscula
print(f"Todos os nomes começam com C? {analise}")






