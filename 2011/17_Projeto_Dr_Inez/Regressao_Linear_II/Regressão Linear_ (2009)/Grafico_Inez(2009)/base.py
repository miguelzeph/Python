#!/usr/bin/python
# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np
import os


diretorio_principal=os.getcwd()
os.chdir('./entrada')
vetor = os.listdir('.')

for n in vetor:
	
	#Restrincao
	
	a=60
	b=425
	
	
	
	arq=open('./'+n,'r')
	ler=arq.readlines()
	arq.close()
	
	
	y=[]
	x=[]
	
	if n == 'foF2.txt':
		
		for i in range(0,len(ler)):
			
			foF2=ler[i][24:30]
			
			if foF2 == '------' or foF2 == 'n__tem':
				
				y.append(None)
			
			else:
				y.append(float(foF2))
	
	if n == 'solar.txt':
		
		#for i in range(0,len(ler)):
		for i in range(a,b):
			
			flux=ler[i][17:21]
			
			x.append(float(flux))	