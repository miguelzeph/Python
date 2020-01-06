#!/usr/bin/python
# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np
import os
from matplotlib.ticker import MultipleLocator


diretorio_principal=os.getcwd()
os.chdir('./entrada')
vetor = os.listdir('.')

if vetor[0] == 'foF2.txt':
	
	
	
	
	arq=open('./'+vetor[0],'r')
	ler=arq.readlines()
	arq.close()
	
	
	y=[]
	
	
	
		
	for i in range(0,len(ler)):
			
		foF2=ler[i][20:26]
			
		if foF2 == '   ---':
				
			y.append(None)
			
		else:
			y.append(float(foF2))

	
if vetor[1] == 'solar.txt':
	#Restrincao
	arq=open('./'+vetor[1],'r')
	ler=arq.readlines()
	arq.close()
	
	a=32
	b=398
	
	x=[]
	y1=[]
	
	#for i in range(0,len(ler)):
	for i in range(a,b):
		
		
		foF2=y[i-32]
		flux=ler[i][17:21]
		
		#print (foF2,flux)
		
		#raw_input()
		
		if (int(flux) < 660 or int(flux) > 780):
			continue
		elif foF2 == None:
			continue
		
		else:
			x.append(int(flux)/10.0)
			y1.append(foF2)

		
		
		
#for j in range(0,365):
#	print x[j],y[j]




B=[]
A=[]

for i in range (0,len(x)):
	
	#if ((x[i] == None )or (y[i] == None)):
	#	continue
	
	#else:
	
	b= ((x[i]-np.mean(x))*(y1[i]-np.mean(y1)))/(x[i]-np.mean(x))**2
	a = np.mean(y1) - b*np.mean(x)
		
	B.append(b)
	A.append(a)

#print B
#print A		
#raw_input()

b = np.mean(B)
a = np.mean(A)

t = np.arange(66,78,1)

s = a + b*t

os.chdir(diretorio_principal)
os.chdir('./saida')

plt.figure(num=1,figsize=(20,10))


plt.rcParams["xtick.major.size"]=10
plt.rcParams["xtick.minor.size"]=5
plt.rcParams["ytick.major.size"]=10
plt.rcParams["ytick.minor.size"]=5
		
sub1=plt.subplot(1,1,1)

x_maior=2
x_menor=1
y_maior=1
y_menor=0.5
		
sub1.xaxis.set_major_locator(MultipleLocator(x_maior))
sub1.xaxis.set_minor_locator(MultipleLocator(x_menor))
		
sub1.yaxis.set_major_locator(MultipleLocator(y_maior))
sub1.yaxis.set_minor_locator(MultipleLocator(y_menor))



plt.xlabel('Fluxo Solar')
plt.ylabel('foF2(MHz)')
plt.title('Grafico_Teste')
plt.plot(x,y1,'ro',lw=2,label=u"Fev 1996  - Jan 1997")
plt.plot(t,s,'r-',lw=2,label=u'Regressão Linear Simples')
plt.legend().get_frame().set_facecolor('0.95')
plt.ylim(3.5,13.5)
plt.xlim(66,78)
plt.grid(True)
plt.show()
#plt.savefig('./grafico_teste.png')	
