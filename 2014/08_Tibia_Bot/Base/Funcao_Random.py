import random

sorteio=rm.choice#faz um sorteiro... e escolhe um valor dentro do nosso vetor a

a=[]

for i in range(0,5):
	a.append(raw_input('Nome dos candidatos '+str(i+1)+ ' : '))

print u"Os candidatos são:",a

sorteado=sorteio(a)#ou podiacolocar rm.choice(a)

print u"o grande vencedor do sorteio é :",sorteado

raw_input()
