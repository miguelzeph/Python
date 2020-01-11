from __future__ import division
import os
import matplotlib.pyplot as plt
import numpy as np

diretorio_principal = os.getcwd()
	

os.chdir('dados')
	
#-------- ENCONTRAR ARQUIVO TXT NO DIRETORIO-------

lista = os.listdir('.')
txts = []

for i in range(0,len(lista)):
	if (lista[i].find('.txt') == -1 and lista[i].find('.csv') == -1 ):#find quando n tem ele retorna -1
		continue
	else:
		txts.append(lista[i])
#-------------------------------------------------


#vetores	


for arquivo in range(0,len(txts)):
	
	arq_entrada=open(txts[arquivo],'r')
	arq_dados=arq_entrada.readlines()
	arq_entrada.close()
	
	f_v=[]
	e1_v=[]
	e2_v=[]
	u1_v=[]
	u2_v=[]	

	z_v=[]

	for i in range(8,len(arq_dados)):
		dados = arq_dados[i].split(',')
		
		f_v.append(dados[0])
		e1_v.append(dados[1])
		e2_v.append(dados[2])
		u1_v.append(dados[3])
		u2_v.append(dados[4])
		
		f = float(dados[0])
		e1= float(dados[1])
		e2= float(dados[2])
		u1= float(dados[3])
		u2= float(dados[4])
		
		
		e=(e1**2+e2**2)**(1.0/2.0)
		u=(u1**2+u2**2)**(1.0/2.0)
		lamb = 3e8/f #m
		d = 0.0015#metros
		z = abs(((u/e)**(1.0/2.0))*np.tanh(((2*np.pi*d/lamb)*((u/e)**(1.0/2.0)))*1j))
		
		z_v.append(z)
	plt.title(str(txts[arquivo][:len(txts[arquivo])-4]))	
	plt.plot(f_v,z_v,'-b')
	plt.show()
	
	#plt.close()


