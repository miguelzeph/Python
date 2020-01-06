# -*- coding: utf-8 -*-
import os
saida='./saida/gama.txt'
arq_saida=open(saida,'w')
for d in range(1,32):
	if d <=9:
		dia='0'+str(d)
	else:
		dia=str(d)
	entrada='./entrada/gama_10_12_'+str(dia)+'.txt'
	if os.path.exists(entrada):
		arq_entrada=open(entrada,'r')
		arq_dados=arq_entrada.readlines()
		arq_entrada.close()
		
				
		for linha in range(4,len(arq_dados)):
			data=arq_dados[linha][0:13]
			dose=arq_dados[linha][13:21]
			
				
			escrever="%s %s\n" %(data,dose)#filtro para tirar erros
			arq_saida.write(escrever)
	else:
		continue
arq_saida.close()