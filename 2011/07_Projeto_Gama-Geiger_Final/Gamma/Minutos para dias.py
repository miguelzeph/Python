# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator
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
				if (float(dose) >= 0.25 and float(dose) <= 0.4):
					y.append(float(dose))
				else:
					y.append(0.33)
			y1.extend(y)#otima func, ela que add os valores ao novo vetor.
	
	
	#x=np.arange(0,len(y1))
	x=np.arange(0,float(len(y1))/143.0,1.0/143.0)
	
	#media=[(sum(y1)/len(y1))]*(len(y1))
	media=[np.mean(y1)]*len(y1)
	dp=np.std(y1)
	
	
	os.chdir(diretorio_principal)
	
	
	
		
	os.chdir(diretorio_principal)	
	
	if int(n) == 10:
		
		
		
		a=smoothListGaussian(y1)#valores do smoothing
		x1=np.arange(0,float(len(a))/143.0,1.0/143.0)
		
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
		
		
		
		plt.plot(x,y1,'k-',label=' Gamma-Geiger')
		plt.plot(x1,a,'b-',label=u" Média de "+str(n)+" Minutos",lw=2)
		continue
	
	else:
		
		b=smoothListGaussian(y1)#valores do smoothing
		
		x2=np.arange(0,float(len(b))/143.0,1.0/143.0)
		
		plt.ylabel(ur'Dose de Radiação ($\mu$S/h)',fontsize=15)
		#plt.ylabel(r'$\mu$') , dica
		plt.xlabel('Dias',fontsize=15) 
		plt.title(u'São José dos Campos - Verão - Janeiro_Fevereiro de 2008',fontsize=15)	
		
		
		plt.ylim(0.2,0.5)
		plt.xlim(0,46)
		plt.plot(x2,b,'r-',label=u" Média de "+str(n)+" Minutos",lw=2)
		
		
		dp=str(dp)
		esc=dp[0:5]
		
		
		media=str(media[0])
		media=media[0:5]
		#print media
		escrever=str(media)
		media=[float(media)]*(len(y1))
		plt.plot(x,media,'g',lw=3,label=ur'Média,D.P=('+escrever+','+esc+')$\mu$S/h')
		#plt.plot(10,10,'r.',lw=0,label=u'Desvio Padrão='+esc+'$\mu$S/h')
		plt.legend().get_frame().set_facecolor('0.95')
		
		#plt.text(-300,0.63,'Contagens de 10 min')
		plt.text(1,0.17,u'Início: Hora Local 22:04, 10/01/08')
		plt.text(34,0.17,'Fim: Hora Local 00:09, 26/02/08')
		
		
		
		plt.grid(True)
		
		
	
		
				
os.chdir('./saida_graficos')
plt.savefig(u'Grafico_Escala_novas.png')
#plt.show()
