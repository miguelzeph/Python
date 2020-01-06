#!/usr/bin/python
# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np
import os


diretorio_principal=os.getcwd()

os.chdir('./saida')
dado=open('./dados.txt','w')
dado.write(' Data  Fluxo     foF2 \n')

os.chdir(diretorio_principal)
os.chdir('./entrada')
vetor = os.listdir('.')




if vetor[0] == 'foF2.txt':
	
	
	
	
	arq=open('./'+vetor[0],'r')
	ler=arq.readlines()
	arq.close()
	
	
	y=[]
	
	
	
		
	for i in range(0,len(ler)):
			
		foF2=ler[i][24:30]
			
		if foF2 == '------' or foF2 == 'n__tem':
				
			y.append(None)
			
		else:
			y.append(float(foF2))

	
if vetor[1] == 'solar.txt':
	#Restrincao
	arq=open('./'+vetor[1],'r')
	ler=arq.readlines()
	arq.close()
	
	a=0
	b=366
	
	x=[]	
	
	#for i in range(0,len(ler)):
	for i in range(a,b):
			
		flux=ler[i][17:21]
		x.append(int(flux))

		
ano = '09'	
dia = 1	
for j in range(0,366):
	
	
	#if dia > 365:
	#	dia = 1
	#	ano = '10'
	
	a=(x[j]) 
	b=(y[j])
	
	if b == None:
		b='----'
		linha = '%s_%03d  %4d    %6s\n'%(ano,dia,a,b)
		dado.write(linha)
	else:
		b=b
	
		linha = '%s_%03d  %4d    %6.3f\n'%(ano,dia,a,b)
		dado.write(linha)
	dia =dia+1

os.chdir(diretorio_principal)	
os.chdir('./saida')
dado.close()
	

