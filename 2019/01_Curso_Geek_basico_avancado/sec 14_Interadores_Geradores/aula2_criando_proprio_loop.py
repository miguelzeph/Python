"""
Criando os Próprios Loop
"""

#Criei meu Loop...
def meu_for(interavel):

    it = iter(interavel)

    while True:
        try:
            print(next(it))
        except StopIteration:
            break
meu_for('Miguel')
meu_for([1,2,3,4,5])

