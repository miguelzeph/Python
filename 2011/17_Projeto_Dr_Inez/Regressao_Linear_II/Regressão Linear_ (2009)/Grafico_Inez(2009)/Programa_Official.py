#!/usr/bin/python
# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np
import os


diretorio_principal=os.getcwd()
os.chdir('./entrada')
vetor = os.listdir('.')

if vetor[0] == 'foF2.txt':
	
	
	
	
	arq=open('./'+vetor[0],'r')
	ler=arq.readlines()
	arq.close()
	
	
	y=[]
	
	
	
		
	for i in range(0,len(ler)):
			
		foF2=ler[i][24:30]
			
		if foF2 == '------' or foF2 == 'n__tem':
				
			y.append(None)
			
		else:
			y.append(float(foF2))

	
if vetor[1] == 'solar.txt':
	#Restrincao
	arq=open('./'+vetor[1],'r')
	ler=arq.readlines()
	arq.close()
	
	a=60
	b=425
	
	x=[]	
	
	#for i in range(0,len(ler)):
	for i in range(a,b):
			
		flux=ler[i][17:21]
		x.append(int(flux))

		
		
		
#for j in range(0,365):
#	print x[j],y[j]



os.chdir(diretorio_principal)
os.chdir('./saida')


plt.xlabel('Fluxo Solar')
plt.ylabel('foF2(MHz)')
plt.title('Grafico_Teste')
#plt.plot(x[0:20],y[0:20],'r')
plt.plot(x,y,'b.')
plt.grid(True)
#plt.show()
plt.savefig('./grafico_teste.png')	
