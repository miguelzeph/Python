from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as si

arq_entrada=open('./raman_dados.txt','r')
arq_dados=arq_entrada.readlines()
arq_entrada.close()

x = []
y = []

for i in range(0,len(arq_dados)):
	
	vetor = arq_dados[i].split(',')
	x.append(float(vetor[0]))
	y.append(float(vetor[1]))

offset = 8.3

DR=[]#numero d ondas exp
IR=[]#intensidade experi


for j in range(0,101):

	DR.append(x[j+180-1]+offset)
	
	IR.append(y[j+180-1]-(0.095*x[j+180-1]-20.665)-30)

# L = valor de entrada para o diametro do cristalite que deve ser
# fitrado inicialmente por processo manual e depois devera ser
# introduzido um loop com calculo do chi**2 , L e dado em undade
# do parametro de rede do Si cristalino (a=0.54nm)

# wo = Valor de entrada para o shift central do pico
# de primeira ordem que devera ser fitrado inicialmente
# por processo manual d depois devera ser introduzido um loop
# com calculo do chi**2
# w0 = 520.5 para determinar o wconf

# Gama = valor de entrada para largura de linha do pico de primeira
# ordem do espectro de espalhamento Raman que devera ser fitado
# inicialmente por processo manual e depois devera ser introduzido
# um loop com calculo do chi2
# O ajuste e bem pequeno pois corresponde a largura da linha do
# pico de primeira ordem para o Si cristalino que deve ester por
# volta de 4,5 cm-1 (esta na tese ... determina o wconf)


L = 19 
wo = 521 #valor de x correspondente ao pico 1830 de y
Gama = 6.2 # 4.5 determina o wconf

def raman0(x,L,w0,wo,Gama):
	return ((np.exp(-(x**2)*(L**2)/4))*(x**2)*4*np.pi)/(((w0-(wo-120*(x**2)))**2)+((Gama/2)**2))

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


#-------------------------------Silicio Amorfo-------------------
Gamorfo=[] # variavel que sera calculada pelo programa que ajustara 
		   #a gaussiana correspondente ao silicio amorfo
w0 = DR[i]
A=0.35e4 #amplitude da gaussiana	
#ajuste manual , deve ser preparado um loop para o ajuste
wa=501	#w (deslocamento raman) central da gaussiana
#ajuste manual , deve ser preparado um loop para o ajuste
gamaa=37 #largura da linha da gaussiana
#ajuste manual , deve ser preparado um loop para o ajuste

for i in range(0,101):
	#Calcula a gaussiana do Si amorfo
	k = A*(np.exp(-2*((w0-wa)**2)/gamaa**2))/(gamaa*np.sqrt(np.pi/2))
	Gamorfo.append(k)
#----------------------------------------------------------------

IRR = IR               #intensidade experimental
QT0max = max(QTY) 
IRRmax = max(IRR)
Io=IRRmax/QT0max 

def raman1(x,Io,L,w,wo,Gama):
	return Io*((np.exp(-(x**2)*(L**2)/4))*(x**2)*4*np.pi)/(((w-(wo-120*(x**2)))**2)+((Gama/2)**2))


QTX1=QTX#=DR
QTY1=[]

for i in range(0,101):
	
	w=DR[i]
	args1=(Io,L,w,wo,Gama)
	a = 0
	b = 1
	Q = si.quadrature(raman1,a,b,args1)#Segunda Integral ******
	QTY1.append(Q[0]) #integral
	#QTY1.append(Q[0]+Gamorfo[i]) assim soma a parte amorfa junto
	#na tese diz nao modificar muito, apenas em alguns casos
	
	
#intensidade Teorica
IT = QTY1

plt.plot(DR,IT,'b+',label='Teorico',)
plt.plot(DR,IR,'r.',label='Experimental')
plt.xlabel('Raman Shit (1/cm)')
plt.ylabel('Intensity (a.u)')
plt.legend()
plt.grid(True)	
plt.show()