#!/usr/bin/python
# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np
import os
from matplotlib.ticker import MultipleLocator


diretorio_principal=os.getcwd()
os.chdir('./entrada_1')
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

Q = np.arange(66,78,1)

s = a + b*Q


os.chdir(diretorio_principal)
