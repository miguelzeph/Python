# -*- coding: utf-8 -*-

import os

#Função para juntar o arquivo atual
def juntar_atual(ano,mes,dia,lugar):
	entrada='./entrada/gama_'+ano+'_'+mes+'_'+dia+'_'+lugar+'.txt'
	if os.path.exists(entrada):
		arq_entrada=open(entrada,'r')
		arq_dados=arq_entrada.readlines()
		arq_entrada.close()
		
		#x=[]
		#y=[]
		
		for linha in range(0,len(arq_dados)):
			#atual=arq_dados[linha]
			arq_saida.write(arq_dados[linha])
			#vetor_cols=atual.split('\t')
			#x_atual=vetor_cols[0]
			#y_atual=vetor_cols[1]
			#x.append(x_atual)
			#y.append(y_atual)
			#x.append(arq_dados[linha].split('\t')[0])
			#y.append(arq_dados[linha].split('\t')[1])
	return	

#Programa principal

saida='./saida/gama.txt'
arq_saida=open(saida,'w')

for a in range(6,12):
	if a < 10:
		ano='0'+str(a)
	else:
		ano=str(a)
	
	for m in range(1,13):
		if m < 10:
			mes='0'+str(m)
		else:
			mes=str(m)
		
		for d in range(1,32):
			if d < 10:
				dia='0'+str(d)
			else:
				dia=str(d)
			
			for lugar in ('ITA','CASA'):
				juntar_atual(ano,mes,dia,lugar)

arq_saida.close()