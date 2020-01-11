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


	


for arquivo in range(0,len(txts)):
	
	arq_entrada=open(txts[arquivo],'r')
	arq_dados=arq_entrada.readlines()
	arq_entrada.close()
	
	
	#vetores --------
	f_v=[]
	e1_v=[]
	e2_v=[]
	u1_v=[]
	u2_v=[]	

	z_v=[]
	
	reflection_v =[]
	
	porcentagem_v =[]
	#----------------
	
	
	arq = open('./teorico_'+txts[arquivo],'w')
	arq.write("Freq(Hz)	RL(%)\n")
	
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
		
		c = 3e8
		e=e1+e2*1j #AGORA ESTA CERTO!!! TEM QUE SER REAL E IMAGINARIO
		u=u1+u2*1j #AGORA ESTA CERTO!!! TEM QUE SER REAL E IMAGINARIO
		d = 0.0015#metros
		
		#---------Ate aqui e DB negativo---------------------------------------
		z = ((u/e)**(1.0/2.0))*np.tanh(1j*(2*np.pi*f*d/c)*((u*e)**(1.0/2.0)))
		
		z_v.append(z)
		
		reflection = -2*20*np.log10(abs((z-1)/(z+1)))
		
		reflection_v.append(reflection)
		#-----------------------------------------------------------------------
		
		#-------Aqui eu passo para RL(%)----------------------------------------
		
		porcent = (10.0**((reflection/10.0)))*100.0-100.0
		
		porcentagem_v.append(porcent)
		
		#-----------------------------------------------------------------------
		
		#escrever = "%s	%s\n"%(f,reflection)
		escrever = "%s	%s\n"%(f,porcent)
		
		arq.write(escrever)
		
	arq.close()		
			
	plt.title(str(txts[arquivo][:len(txts[arquivo])-4]))	
	#plt.plot(f_v,reflection_v,'-b')
	plt.plot(f_v,porcentagem_v,'-b')
	
	plt.xlim(8.2e9,12.4e9)
	


	plt.show()
	
	#plt.close()


