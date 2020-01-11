# -*- coding: utf-8 -*-

import os

diretorio_principal=os.getcwd()
os.chdir('./entrada')
lista=os.listdir('.')
txts=[]

for i in range(0,len(lista)):
	if (lista[i].find('.ASC') == -1):#find quando n?tem ele retorna -1
		continue
	else:
		txts.append(lista[i])
		
RAMAN=[]
INTENSIDADE=[]

for arquivo in range(0,len(txts)):
	
	arq_saida=open(txts[arquivo].split('.')[0]+'.txt','w')
	
	arq_entrada=open(txts[arquivo],'r')
	arq_dados=arq_entrada.readlines()
	arq_entrada.close()
	
	
	for linha in range(0,len(arq_dados)):
		
		dados= arq_dados[linha].split(' ')
		while True:
			try:
				dados.remove('')
			except ValueError:
				break
		
		try:
			
			INTENSIDADE.append(dados[1])
			RAMAN.append(dados[0])
		except IndexError:
			break
		
	for i in range(0,len(RAMAN)):

		escrever = "%s%s" % (RAMAN[i],INTENSIDADE[i])
		arq_saida.write(escrever)
		
	RAMAN=[]
	INTENSIDADE=[]
		
arq_saida.close()

lista=os.listdir('.')
txts=[]

for i in range(0,len(lista)):
	if (lista[i].find('.txt') == -1):#find quando n?tem ele retorna -1
		continue
	else:
		txts.append(lista[i])

os.chdir(diretorio_principal)
saida='./saida/'+txts[0].split("_")[0]+'.txt'
arq_saida=open(saida,'w')

os.chdir(diretorio_principal)
os.chdir('./entrada')

RAMAN =[]
INTENSIDADE =[]

for arquivo in range(0,len(txts)):

	arq_entrada=open(txts[arquivo],'r')
	arq_dados=arq_entrada.readlines()
	arq_entrada.close()
	
	txts_n = txts[arquivo].split("_")
	
	k= int(txts_n[1][0:1])
	
	n=0
	
	if k > 1:
		
		while True:
			
			dadoss = arq_dados[n].split(',')
			
		
			intensidade= dadoss[1]
			raman= dadoss[0]
			
			if float(RAMAN[len(RAMAN)-1]) < float(raman):
			
				constante = float(INTENSIDADE[len(INTENSIDADE)-1]) - float(intensidade)
				
				break
			
			else:
				n=n+1
				

	for linha in range(0,len(arq_dados)):
		
		
		dados= arq_dados[linha].split(',')
		raman= dados[0]
		intensidade= dados[1]
			
	
		if RAMAN == []:
			
			RAMAN.append(float(raman))
			
			
			INTENSIDADE.append(float(intensidade))
			
		if float(RAMAN[len(RAMAN)-1]) < float(raman):
			
			if k > 1:
				
				RAMAN.append(float(raman))
				INTENSIDADE.append(float(intensidade)+constante)
				
			else:
			
				RAMAN.append(float(raman))
				INTENSIDADE.append(float(intensidade))
				
for i in range(0,len(RAMAN)):

	escrever = "%.5f	%.5f\n" % (RAMAN[i],INTENSIDADE[i])
	arq_saida.write(escrever)
	
arq_saida.close()

for j in range(0,len(txts)):
	os.system("del "+txts[j])