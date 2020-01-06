from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as si
import os

arq_entrada=open('./AMOSTRAL(ARRUMAD).txt','r')
arq_dados=arq_entrada.readlines()
arq_entrada.close()


def raman0(x,L,w0,wo,Gama):
	return ((np.exp(-(x**2)*(L**2)/4))*(x**2)*4*np.pi)/(((w0-(wo-120*(x**2)))**2)+((Gama/2)**2))


def raman1(x,Io,L,w,wo,Gama):
	return Io*((np.exp(-(x**2)*(L**2)/4))*(x**2)*4*np.pi)/(((w-(wo-120*(x**2)))**2)+((Gama/2)**2))


x = []
y = []



for i in range(0,len(arq_dados)):
	
	vetor = arq_dados[i].split(' ')
	
	x.append(float(vetor[0]))
	
	y.append(float(vetor[1]))

#offset = 8.3 #obs 10 fica bom

#intensidade experi

os.chdir('./Grafico')

for offset in np.arange(30,40,1):
	DR=[]#numero d ondas exp
	IR=[]
	#antes = for j in range(0,len(x)):
	for j in range(0,len(arq_dados)):

		DR.append(x[j]+offset)
		
		
		#IR.append(y[j]-(0.095*x[j]-20.665)-30)
		IR.append(y[j])


	L = 19
	wo = 521
	Gama = 6.2



	QTX=DR
	QTY=[]



	for i in range(0,len(arq_dados)):
			
			
			
			
		w0 = DR[i]
			
		a = 0
		b = 1
			
		args0=(L,w0,wo,Gama)
			
		Q0= si.quadrature(raman0,a,b,args0)# primeira Integral*****
			
		#QTX.append(w0)
			
			
		QTY.append(Q0[0])
			
			
			
			



		

	IRR = IR               #intensidade experimental
	QT0max = max(QTY) 

	IRRmax = max(IRR)

	Io=IRRmax/QT0max 




	QTX1=QTX#=DR
	QTY1=[]

		

	for i in range(0,len(arq_dados)):
		#teste = ler[i].split(' ')---------
			
		w=DR[i]
			
		args1=(Io,L,w,wo,Gama)
		a = 0
		b = 1
		Q = si.quadrature(raman1,a,b,args1)#Segunda Integral ******
		QTY1.append(Q[0])#integral
			
		
	IT = QTY1



	plt.plot(DR,IT,'b+',label='offset = '+str(offset))

	plt.plot(DR,IR,'r.',label='Experimental')
	
	plt.xlabel('Raman Shit (1/cm)')
	plt.ylabel('Intensity (a.u)')
	plt.legend()
	plt.xlim(480,550)
	plt.grid(True)	
	if offset < 10:
		plt.savefig('./grafico_'+'0'+str(offset)+'.png')
	
	if (offset < 0 and offset > -10):
		plt.savefig('./grafico_'+'0'+str(offset)+'.png')
		
	if (offset < -10):
		plt.savefig('./grafico_'+str(offset)+'.png')
		
	if offset >=10: 
		plt.savefig('./grafico_'+str(offset)+'.png')
	plt.close()
