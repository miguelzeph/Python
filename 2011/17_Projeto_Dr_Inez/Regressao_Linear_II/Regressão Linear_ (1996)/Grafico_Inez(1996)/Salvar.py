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
	
	x   =[]	
	ano =[]
	dia =[]
	
	#for i in range(0,len(ler)):
	for i in range(a,b):
			
		flux=ler[i][17:21]
		ano_ =ler[i][0:4]
		dia_ =ler[i][11:15]
		
		x.append(int(flux))
		ano.append(int(ano_))
		dia.append(int(dia_))

	
for j in range(0,367):
	
	
	#if dia > 365:
	#	dia = 1
	#	ano = '10'
	
	a=(x[j]) 
	b=(y[j])
	c=(ano[j])
	d=int((dia[j]))
	
	if b == None:
		b='----'
		linha = '%s_%03d  %4d    %6s\n'%(c,d,a,b)
		dado.write(linha)
	else:
		b=b
	
		linha = '%s_%03d  %4d    %6.3f\n'%(c,d,a,b)
		dado.write(linha)

os.chdir(diretorio_principal)	
os.chdir('./saida')
dado.close()
	

