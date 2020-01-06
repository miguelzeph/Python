# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np
import os

for n in ('10','60'):
	
	def smoothListGaussian(list,strippedXs=False,degree=int(n)):
		window=degree*2-1  
		weight=np.array([1.0]*window)  
		weightGauss=[]  
		for i in range(window):  
			i=i-degree+1  
			frac=i/float(window)  
			gauss=1/(np.exp((4*(frac))**2))  
			weightGauss.append(gauss)  
		weight=np.array(weightGauss)*weight  
		smoothed=[0.0]*(len(list)-window)  
		for i in range(len(smoothed)):  
			smoothed[i]=sum(np.array(list[i:i+window])*weight)/sum(weight)  
		return smoothed  



	diretorio_principal=os.getcwd()
	os.chdir('./entrada')
	lista=os.listdir('.')
	txts=[]


	for i in range(0,len(lista)):
		if (lista[i].find('GAMMA') == -1):#find quando n?tem ele retorna -1
			continue
		else:
			txts.append(lista[i])
		
		y1=[]
		for p in range(0,len(txts)):
			
			arq_entrada=open(txts[p],'r')
			arq_dados=arq_entrada.readlines()
			arq_entrada.close()
			
			
			y=[]
				
			for linha in range(26,len(arq_dados)-1):
					
					dose=arq_dados[linha].split('\t')[6][0:5]
					y.append(float(dose))	
			y1.extend(y)#otima func, ela que add os valores ao novo vetor.

	
	x=np.arange(0,len(y1))
	
	
	os.chdir(diretorio_principal)
	
	
		
	os.chdir(diretorio_principal)	
	
	if int(n) == 10:
		plt.plot(x,y1,'k-',label='Gamma')
		plt.plot(smoothListGaussian(y1),'b-',label=u"Média de "+str(n)+" Minutos")
		continue
	
	else:
		
		plt.ylabel(u'Dose de Radiação (MicroSievert/Hora)')
		plt.xlabel('Tempo em Minutos') 
		plt.title(u'Gráfico de Radiação')	
		
		plt.plot(smoothListGaussian(y1),'r-',label=u"Média de "+str(n)+" Minutos")
		plt.legend()
		plt.grid(True)
	
	
	
os.chdir('./saida_graficos')	
plt.savefig(u'Grafico.png')
