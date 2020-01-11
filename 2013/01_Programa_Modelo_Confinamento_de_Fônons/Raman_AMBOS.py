from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as si
from matplotlib.widgets import Slider, Button, RadioButtons
#from matplotlib.ticker import MultipleLocator
import os

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
		
		vetor = arq_dados[i].split(' ')
		
		x.append(float(vetor[0]))
		
		y.append(float(vetor[1]))

	DR=[]#numero d ondas exp
	IR_I=[]#intensidade experi


	for j in range(0,len(arq_dados)):

		DR.append(x[j])
		IR_I.append(y[j])

		
	#----------NORMAIZAR_ Y --------------
	IR=[]

	for i in range(0,len(arq_dados)):
		
		I = IR_I[i]/max(IR_I)
		#I=IR_I[i]

		IR.append(I)
		
	#------------------------------------	
	#chutes----------------------
	L = 19

	#fixo
	for i in range(0,len(IR)):
		
		if IR[i] == max(IR):
					
			wo= DR[i]
					
	#wo = 515
	Gama = 6.2
	#---------------------------


	os.chdir(principal)


	def raman0(x,L,w0,wo,Gama):
		return ((np.exp(-(x**2)*(L**2)/4))*(x**2)*4*np.pi)/(((w0-(wo-120*(x**2)))**2)+((Gama/2)**2))

	QTX=DR
	QTY=[]

	for i in range(0,len(DR)):	
		
		w0 = DR[i]
		
		a = 0
		b = 1
		
		args0=(L,w0,wo,Gama)
		
		Q0= si.quad(raman0,a,b,args0)
		
		
		
		QTY.append(Q0[0])


	IRR = IR               
	QT0max = max(QTY) 

	IRRmax = max(IRR)

	Io=IRRmax/QT0max 

	def raman1(x,Io,L,w,wo,Gama):
		return Io*((np.exp(-(x**2)*(L**2)/4))*(x**2)*4*np.pi)/(((w-(wo-120*(x**2)))**2)+((Gama/2)**2))


	QTX1=QTX#=DR
	QTY1=[]



	for i in range(0,len(DR)):
		
		w=DR[i]
		
		args1=(Io,L,w,wo,Gama)
		a = 0
		b = 1
		Q = si.quad(raman1,a,b,args1)
		QTY1.append(Q[0])

	IT = QTY1	

		
	#calculo Amorfo----------------------------------------

	A=1   #0.35e4	
	wa=500	
	gamaa=37


	Gamorfo_I=[]


	for i in range(0,len(DR)):
		
		w0=DR[i]
		#equacao de uma gaussiana...
		k = A*(np.exp(-2*((w0-wa)**2)/gamaa**2))/(gamaa*np.sqrt(np.pi/2))
		Gamorfo_I.append(k)                                         

	# nao precisa normalizar, o valor de A e para isto

	#------------------------------------	

	#-------GRAFICO1----------------------------------------
	ax1= plt.subplot(121)
	plt.subplots_adjust(left=0.05,right=0.98, bottom=0.3,top=0.94)
	k, =plt.plot(DR,IT,'b*',label='Teorico')
	u, =plt.plot(DR,Gamorfo_I,'g*',label='Amorfo',)
	plt.plot(DR,IR,'r.',label='Experimental')
	plt.title("Cristalino e Amorfo")

	#copy;;;;
	plt.xlabel('Raman Shit (1/cm)')
	plt.ylabel('Intensity (a.u)')
	plt.ylim(0.0,1.1)

	plt.legend()
	plt.grid(True)
	#;;;;;



	#Soma das Intensidades

	I_TOTAL=[]

	for i in range(0,len(DR)):
		
		I_TOTAL.append(IT[i]+Gamorfo_I[i])

		


	#-----GRAFICO2 Total-------------------------------------------

	ax2=plt.subplot(1,2,2)

	t, =plt.plot(DR,I_TOTAL,'b-',label='Curva Total')
	plt.plot(DR,IR,'r.',label='Experimental')
	
	
	
	#new
	fig_text = plt.figtext(0.58, 0.8,  str('Chi-q =...'))
	
	
	
	#copy;;;;
	plt.xlabel('Raman Shit (1/cm)')
	plt.ylabel('Intensity (a.u)')
	plt.ylim(0.0,1.1)
	plt.title("Total - Amostra " +txts[n][0:(len(txts[n])-4)])

	plt.legend()
	plt.grid(True)
	#copy;;;;

	#---------------------------------------------------------

	#programa interacao****************************)))))))--------------------------------------------------
	axcolor=(0.5,0.7,0.7)

	wo_ = plt.axes([0.1, 0.15, 0.3, 0.03], axisbg=axcolor)
	L_ = plt.axes([0.1, 0.05, 0.3, 0.03], axisbg=axcolor)#(pos(x da barra),pos(y da barra),comprimento,largura)
	GAMA_  = plt.axes([0.1, 0.10, 0.3, 0.03], axisbg=axcolor)


	li=5
	lf=100

	woi=512
	wof=525

	gi=3
	gf=8

	lbar= Slider(L_, 'L (a.nm)', li, lf, valinit=L)
	wobar= Slider(wo_, 'wo (1/cm)', woi, wof, valinit=wo)
	gamabar = Slider(GAMA_, 'Gama (1/cm)', gi, gf, valinit=Gama)


	#amorfo
	wo_am = plt.axes([0.6, 0.15, 0.3, 0.03], axisbg=axcolor)
	A_am = plt.axes([0.6, 0.05, 0.3, 0.03], axisbg=axcolor)#(pos(x da barra),pos(y da barra),comprimento,largura)
	GAMA_am = plt.axes([0.6, 0.10, 0.3, 0.03], axisbg=axcolor)


	Ai_am=0.001
	Af_am=5

	woi_am=450
	wof_am=515

	gi_am=20
	gf_am=40


	Abar_am= Slider(A_am,'A' ,Ai_am, Af_am, valinit=A)
	wobar_am= Slider(wo_am,'wo_A (1/cm)' ,woi_am, wof_am, valinit=wa)
	gamabar_am = Slider(GAMA_am, 'Gama_A (1/cm)', gi_am, gf_am, valinit=gamaa)


	#Grafico1----------------------------------------------------
	def update1(val):#este val nao tem nada a ver com ...
							#
							#
		Gama = gamabar.val # este val...
		L = lbar.val
		wo = wobar.val
		#criar um deff ***********************
		QTY=[]
		for i in range(0,len(DR)):	
			
			w0 = DR[i]
			
			a = 0
			b = 1
			
			args0=(L,w0,wo,Gama)
			
			Q0= si.quad(raman0,a,b,args0)
			
			QTY.append(Q0[0])


		IRR = IR              
		QT0max = max(QTY) 

		IRRmax = max(IRR)

		Io=IRRmax/QT0max 
		QTX1=QTX#=DR
		QTY1=[]



		for i in range(0,len(DR)):
			
			w=DR[i]
			
			args1=(Io,L,w,wo,Gama)
			a = 0
			b = 1
			Q = si.quad(raman1,a,b,args1)
			QTY1.append(Q[0])
			

		IT = QTY1
		
		k.set_ydata(IT)
		#k.set_color('red')
		
		
		plt.draw()
		
	gamabar.on_changed(update1)
	lbar.on_changed(update1)
	wobar.on_changed(update1)

	#Grafico2(amorfo)-------------------------------------------------

	def update2(val):#este val nao tem nada a ver com ...
		
		
		A=Abar_am.val
		wa=wobar_am.val	
		gamaa=gamabar_am.val

		Gamorfo_I=[]
		
		for i in range(0,len(DR)):
			
			w0=DR[i]
			#equacao de uma gaussiana...
			k = A*(np.exp(-2*((w0-wa)**2)/gamaa**2))/(gamaa*np.sqrt(np.pi/2))
			Gamorfo_I.append(k) 
			
			
		u.set_ydata(Gamorfo_I)
		
		
		plt.draw()
		
	gamabar_am.on_changed(update2)
	Abar_am.on_changed(update2)
	wobar_am.on_changed(update2)

	def update3(val):
		Gama = gamabar.val
		L = lbar.val
		wo = wobar.val
		
		QTY=[]
		for i in range(0,len(DR)):	
			
			w0 = DR[i]
			
			a = 0
			b = 1
			
			args0=(L,w0,wo,Gama)
			
			Q0= si.quad(raman0,a,b,args0)
			
			QTY.append(Q0[0])


		IRR = IR              
		QT0max = max(QTY) 

		IRRmax = max(IRR)

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
		
		
		
		
		A=Abar_am.val
		wa=wobar_am.val	
		gamaa=gamabar_am.val

		Gamorfo_I=[]
		
		for i in range(0,len(DR)):
			
			w0=DR[i]
			
			k = A*(np.exp(-2*((w0-wa)**2)/gamaa**2))/(gamaa*np.sqrt(np.pi/2))
			Gamorfo_I.append(k) 
			
			
		
		
		I_TOTAL=[]

		for i in range(0,len(DR)):
			
			I_TOTAL.append(IT[i]+Gamorfo_I[i])
			
		t.set_ydata(I_TOTAL)
		
		execfile('./chi-quad_3.py')
		
		plt.draw()

	gamabar_am.on_changed(update3)
	Abar_am.on_changed(update3)
	wobar_am.on_changed(update3)
	gamabar.on_changed(update3)
	lbar.on_changed(update3)
	wobar.on_changed(update3)
		

		
		

	#Reset....
	resetax = plt.axes([0.8, 0.2, 0.1, 0.04]) #posicao do botao...
	button1 = Button(resetax, 'Reset', color=axcolor, hovercolor='0.5')
	def reset(event):
		lbar.reset()
		gamabar.reset()
		wobar.reset()
		
		Abar_am.reset()
		wobar_am.reset()
		gamabar_am.reset()
		

		
	button1.on_clicked(reset) #precisa de um click
	#programa interacao****************************-----------------------))))))))))))))-------------------


	plt.show()
	os.chdir('./Dados')
	os.system('CLS') #nova func