from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as si
import os

arq_entrada=open('./raman_dados.txt','r')
arq_dados=arq_entrada.readlines()
arq_entrada.close()

def raman0(x,L,w0,wo,Gama):
	return ((np.exp(-(x**2)*(L**2)/4))*(x**2)*4*np.pi)/(((w0-(wo-120*(x**2)))**2)+((Gama/2)**2))


def raman1(x,Io,L,w,wo,Gama):
	return Io*((np.exp(-(x**2)*(L**2)/4))*(x**2)*4*np.pi)/(((w-(wo-120*(x**2)))**2)+((Gama/2)**2))


x = []
y = []

for i in range(0,len(arq_dados)):
	
	vetor = arq_dados[i].split(',')
	
	x.append(float(vetor[0]))
	
	y.append(float(vetor[1]))

offset = 8.3 #obs 10 fica bom

DR=[]#numero d ondas exp
IR=[]#intensidade experi

#antes = for j in range(0,len(x)):
for j in range(0,101):

	DR.append(x[j+180-1]+offset)
	
	IR.append(y[j+180-1]-(0.095*x[j+180-1]-20.665)-30)

os.chdir('./Grafico')
#Dados---
l = np.arange(30,36,1)
#N=0
for T in l:
	L = T
	wo = 521
	Gama = 6.2



	QTX=DR
	QTY=[]




	for i in range(0,101):
		
		
		
		
		w0 = DR[i]
		
		a = 0
		b = 1
		
		args0=(L,w0,wo,Gama)
		
		Q0= si.quadrature(raman0,a,b,args0)# primeira Integral*****
		
		#QTX.append(w0)
		
		
		QTY.append(Q0[0])
		
		
		
		



	Gamorfo=[]

	w0 = DR[i]
	A=0.35e4	
	wa=501	
	gamaa=37
	#-------------------------------INUTIL---------------
	#for i in range(0,101):
		
		#k = A*(np.exp(-2*((w0-wa)**2)/gamaa**2))/(gamaa*np.sqrt(np.pi/2))
		#Gamorfo.append(k)
	#----------------------------------------------------

	IRR = IR               #intensidade experimental
	QT0max = max(QTY) 

	IRRmax = max(IRR)

	Io=IRRmax/QT0max 




	QTX1=QTX#=DR
	QTY1=[]

	#test = open('./certo.txt','r')ttttttt
	#ler=test.readlines()ttttttt
	#test.close()ttttt


	


	for i in range(0,101):
		#teste = ler[i].split(' ')---------
		
		w=DR[i]
		
		args1=(Io,L,w,wo,Gama)
		a = 0
		b = 1
		Q = si.quadrature(raman1,a,b,args1)#Segunda Integral ******
		QTY1.append(Q[0])#integral
		
		#QTY1.append(float(teste[0])) tttttttttttttt
		
		
	#intensidade Teorica
	IT = QTY1

	plt.plot(DR,IT,'b+',label='Teorico - L = '+str(L))
	plt.plot(DR,IR,'r.',label='Experimental')
	plt.xlabel('Raman Shit (1/cm)')
	plt.ylabel('Intensity (a.u)')
	plt.legend(loc=2)
	plt.grid(True)	
	#plt.show()
	
	
	if L < 10:
		plt.savefig('./grafico_'+'0'+str(L)+'.png')
	else: 
		plt.savefig('./grafico_'+str(L)+'.png')
	plt.close()
	