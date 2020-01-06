#!/usr/bin/python
# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np
import os

for i in range(14,27):
	
	
	if os.path.exists('./entrada/gama_11_03_'+str(i)+'.txt'):
		
		arquivo=open('./entrada/gama_11_03_'+str(i)+'.txt','r')
		ler=arquivo.readlines()
		arquivo.close()
		
		x=np.arange(4,len(ler))
		
		
		y=[]
		
		for j in range(4,len(ler)):
			
			
			y.append(float(ler[j][13:21]))	
			
		plt.xlabel('tempo em minutos')
		plt.ylabel('Gama (uS/h)')
		plt.title('Grafico de '+str(i)+'_03_10')
		plt.plot(x,y,'r-',lw=0.5,label='geiger')
		#plt.axis([0,float(len(y)),28000,34000])
		plt.axis([0,4500,28500,34500])
		plt.grid(True)
		plt.legend()
		#plt.show()
		plt.savefig('./grafico'+str(i)+'.png')
		plt.close()