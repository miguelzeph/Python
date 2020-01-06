# -*- coding: utf-8 -*-



arq_saida=open('./tirei_erro.txt','w')

arq_velho=open('./saida/gama.txt','r')
ler=arq_velho.readlines()
arq_velho.close()

for i in range (0,len(ler)):
	hora=ler[i][0:5]
	dose=ler[i][6:11]	
	if ((float(dose) > 0.2) and (float(dose) < 0.5)):
		
		linha='%s %s\n' %(hora,dose)
		arq_saida.write(linha)
	else:
		dose='---'
		linha='%s %s\n' %(hora,dose)
		arq_saida.write(linha)
arq_saida.close()