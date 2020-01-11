from __future__ import division
import numpy as np
import scipy.integrate as si
import os

def raman0(x,L,w0,wo,Gama):
	return ((np.exp(-(x**2)*((L)**2)/4))*(x**2)*4*np.pi)/(((w0-(wo-120*(x**2)))**2)+((Gama/2)**2))

def raman1(x,Io,L,w,wo,Gama):
	return Io*((np.exp(-(x**2)*((L)**2)/4))*(x**2)*4*np.pi)/(((w-(wo-120*(x**2)))**2)+((Gama/2)**2))

principal = os.getcwd()
#os.chdir('./dados')
os.chdir('./Dados')

lista=os.listdir('.')
txts=[]

for i in range(0,len(lista)):

	if (lista[i].find('.txt') == -1):
	#if (lista[i].find('.txt') == -1):#find quando n tem ele retorna -1
		continue
	else:
		txts.append(lista[i])
		
for n in range(0,len(txts)):
	arq_entrada=open('./'+txts[n],'r')
	arq_dados=arq_entrada.readlines()
	arq_entrada.close()
	

	x = []
	y = []

	for i in range(0,len(arq_dados)):
		
		vetor = arq_dados[i].split('	')
		
		x.append(float(vetor[0]))
		
		y.append(float(vetor[1]))


	DR=[]
	IR=[]


	for j in range(0,len(arq_dados)):

		DR.append(x[j])
		
		IR.append(y[j])

	a=0.54 #nm Si-c	

	Arm_L=[]
	Arm_Gama=[]
	Arm_wo=[]
	CHI=[]
	chi=0
	os.chdir(principal)
	os.chdir('./Analise')
	V = open('./dados_'+str(txts[n]),'w')
	V.write('L(nm) Gama(1/cm) Wo(1/cm)  Chi-quad\n')

	l=np.arange(5,30,2.5)
	g=np.arange(3,7,0.25)
	W=np.arange(520,523,0.25)

	for cristalito in l:
			
		L = cristalito
		
		

		for largura in g:

			Gama = largura
			
			for pico in W:
			
				wo= pico
				
				#Resolucao da Integral
				
				QTX=DR
				QTY=[]

				for i in range(0,len(DR)):
								
					w0 = DR[i]
					a = 0
					b = 1
					args0=(L,w0,wo,Gama)
					Q0= si.quad(raman0,a,b,args0)# primeira Integral*****
					QTY.append(Q0[0])
						   
				QT0max = max(QTY) 
				IRRmax = max(IR)

				Io=IRRmax/QT0max 
				
				
				QTX1=QTX
				QTY1=[]


				for i in range(0,len(DR)):
					
					w=DR[i]
					
					args1=(Io,L,w,wo,Gama)
					a = 0
					b = 1
					Q = si.quad(raman1,a,b,args1)
					QTY1.append(Q[0])

				IT = QTY1	
			
				#Programa Chi-quad
				
				for i in range(0,len(IT)):
		
					chi= chi + (((IT[i]-IR[i])**2)/IR[i])
				
				grau = chi/len(IR)
				Arm_L.append(L)
				Arm_Gama.append(Gama)
				Arm_wo.append(wo)
				CHI.append(grau)
				
				chi=0 # AQUI ESTA A SOLUCAO...
		
		#Qual o Menor Chi-quad para este valor de L ?
		for j in range(0,len(CHI)):

			if CHI[j] == min(CHI):
							
				gravar ='%4.2f   %2.2f   %4.2f   %f\n'%(Arm_L[j]*0.54,Arm_Gama[j],Arm_wo[j],CHI[j])
				V.write(gravar)
				print gravar
		#Reset		
		Arm_L=[]
		Arm_Gama=[]
		Arm_wo=[]
		CHI=[]
		#chi=0 ENCONTREI O PROBLEMA
	os.chdir(principal)
	os.chdir('./Dados')	
	V.close()