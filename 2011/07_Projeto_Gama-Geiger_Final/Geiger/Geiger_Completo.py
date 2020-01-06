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

	
	x=np.arange(0,len(y1))
	
	media=[(sum(y1)/len(y1))]*(len(y1))
	dp=np.std(y1)
	
	os.chdir(diretorio_principal)
	
	
		
	os.chdir(diretorio_principal)	
	
	if int(n) == 10:
		
		plt.plot(x,y1,'k-',label='Gamma-Geiger')
		plt.plot(smoothListGaussian(y1),'b-',label=u"Média de "+str(n)+" Minutos")
		continue
	
	else:
		
		plt.ylabel(ur'Dose de Radiação ($\mu$S/h)',fontsize=15)
		#plt.ylabel(r'$\mu$') , dica
		plt.xlabel('Tempo em Minutos',fontsize=15) 
		plt.title(u'São José dos Campos - Verão - Dezembro de 2009',fontsize=15)	
		plt.ylim(0.0,0.6)
		plt.plot(smoothListGaussian(y1),'r-',label=u"Média de "+str(n)+" Minutos")
		plt.text(-300,-0.05,u'Início: 11:00, 01/12/09')	
		plt.text(12000,-0.05,'Fim: 00:11, 07/12/09')
		
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
