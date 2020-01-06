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
	
	#for i in range(0,len(ler)):
	for i in range(a,b):
			
		flux=ler[i][17:21]
		x.append(int(flux)/10.0)

		
		
		
#for j in range(0,365):
#	print x[j],y[j]



os.chdir(diretorio_principal)
os.chdir('./saida')

plt.figure(num=1,figsize=(12,6))


plt.rcParams["xtick.major.size"]=10
plt.rcParams["xtick.minor.size"]=5
plt.rcParams["ytick.major.size"]=10
plt.rcParams["ytick.minor.size"]=5
		
sub1=plt.subplot(1,1,1)

x_maior=5
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
plt.plot(x,y,'r.',lw=2,label=u"Fev 1996 - Jan 1997")
plt.legend().get_frame().set_facecolor('0.95')
plt.ylim(3.5,13.5)
plt.xlim(65,100)
plt.grid(True)
plt.show()
#plt.savefig('./grafico_teste.png')	
