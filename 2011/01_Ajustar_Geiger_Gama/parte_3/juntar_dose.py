# -*- coding: utf-8 -*-
import os
saida='./saida/gama.txt'
arq_saida=open(saida,'w')
for d in range(1,23):
	if d <=9:
		dia='0'+str(d)
	else:
		dia=str(d)
	entrada='./entrada/GAMMA_2010_07_'+str(dia)+'.txt'
	if os.path.exists(entrada):
		arq_entrada=open(entrada,'r')
		arq_dados=arq_entrada.readlines()
		arq_entrada.close()
		
				
		for linha in range(26,len(arq_dados)-1):
			dose=arq_dados[linha].split('\t')[6][0:5]
			hora=arq_dados[linha].split('\t')[2][0:2]
			min=arq_dados[linha].split('\t')[2][3:5]
				
			escrever="%s.%s %s\n" %(hora,min,dose)#filtro para tirar erros
			arq_saida.write(escrever)
	else:
		continue
arq_saida.close()