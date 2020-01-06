# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator #quando utiliza o from , não precisa colocar matplotlib.ticker.multiplelocator
import os


for n in ('30','120'):
	
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
		if (lista[i].find('geiger') == -1):#find quando n?tem ele retorna -1
			continue
		else:
			txts.append(lista[i])
		
		y1=[]
		for p in range(0,len(txts)):
			
			arq_entrada=open(txts[p],'r')
			arq_dados=arq_entrada.readlines()
			arq_entrada.close()
			
			
			y=[]
				
			for linha in range(4,len(arq_dados)-1):
					
				dose=arq_dados[linha].split(' ')[1][0:3]
				dados=dose.replace(',','.')
				dados=float(dados)/100
				y.append(float(dados))	
				#if (float(dados) >= 0.2 and float(dados) <= 0.6):
				y.append(dados)
				#else:
					#y.append(0.27) , não precisa do filtro
			y1.extend(y)#otima func, ela que add os valores ao novo vetor.

	
	#x=np.arange(0,len(y1))
	x=np.arange(0,float(len(y1))/1440.0,1.0/1440.0)
	
	media=[(sum(y1)/len(y1))]*(len(y1))
	dp=np.std(y1)
	
	os.chdir(diretorio_principal)
	
	
		
	os.chdir(diretorio_principal)	
	
	if int(n) == 30:
		
		a=smoothListGaussian(y1)#valores do smoothing
		x1=np.arange(0,float(len(a))/1440.0,1.0/1440.0)
		
		plt.figure(num=1,figsize=(12,7))
		
		plt.rcParams["xtick.major.size"]=15
		plt.rcParams["xtick.minor.size"]=8
		plt.rcParams["ytick.major.size"]=15
		plt.rcParams["ytick.minor.size"]=8
		
		sub1=plt.subplot(1,1,1)

		sub1.xaxis.set_major_locator(MultipleLocator(2))
		sub1.xaxis.set_minor_locator(MultipleLocator(1))
		
		sub1.yaxis.set_major_locator(MultipleLocator(0.05))
		sub1.yaxis.set_minor_locator(MultipleLocator(0.025))
		
		plt.plot(x,y1,'k-',label='Gamma-Geiger')
		plt.plot(x1,a,'b-',label=u" Média de "+str(n)+" Minutos",lw=2)
		continue
	
	else:
		
		b=smoothListGaussian(y1)#valores do smoothing
		
		x2=np.arange(0,float(len(b))/1440.0,1.0/1440.0)
		
		plt.ylabel(ur'Dose de Radiação ($\mu$S/h)',fontsize=15)
		#plt.ylabel(r'$\mu$') , dica
		plt.xlabel('Tempo em Minutos',fontsize=15) 
		plt.title(u'São José dos Campos - Verão - Janeiro de 2010',fontsize=15)
		plt.ylim(0,0.6)
		#plt.xlim(0,10)
		plt.plot(x2,b,'r-',label=u" Média de "+str(n)+" Minutos",lw=2)
		
		plt.text(0,-0.05,u'Início: 09:46, 28/12/09')
		plt.text(38,-0.05,'Fim: 09:00, 21/01/10')
		
		dp=str(dp)
		esc=dp[0:5]
		
		media=str(media[0])
		media=media[0:7]
		#print media
		escrever=str(media)
		media=[float(media)]*(len(y1))
		plt.plot(x,media,'g',lw=2,label=ur'Média,D.P=('+escrever+','+esc+')$\mu$S/h')
		
		plt.legend().get_frame().set_facecolor('0.95')
		plt.grid(True)
				
os.chdir('./saida_graficos')
plt.savefig(u'Grafico.png')
