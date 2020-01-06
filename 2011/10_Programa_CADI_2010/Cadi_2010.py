import os 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

diretorio_inicial = os.getcwd()
os.chdir('./entrada')
vetor=os.listdir('.')#ok , leitura está em ordem...


for mes in range(0,4):
	for dia in range(0,32):
		
		nome='CF10'+str(mes)+str(dia)+'.dat'
		
		if os.path.exists(nome):
			arq=open(nome,'r')
			ler=arq.readlines()
			arq.close()
			
			#print nome , veja que está realmente em ordem a leitura...
			
			x=[]
			y=[]
			
			for i in range(2,len(ler)):
				
				hora=float(ler[i][0:5])
				hf=float(ler[i][6:9])
				
				media=(hf+float(ler[i-1][6:9]))/2#criei para dar uma suavizada...
				
				x.append(hora)#add valor do tempo no eixo x...
				
				
				if (media >= 160.0 and media <=330.0):
					
					y.append(media)
					
				else:
					
					y.append(None)
			
			
			os.chdir(diretorio_inicial)#volta para direitorio inicial...
			os.chdir('./saida')#entra no diretorio da pasta saida
			
			#-----escaladas-----------------------------------
			sub1=plt.subplot(1,1,1)

			sub1.xaxis.set_major_locator(MultipleLocator(2))
			sub1.xaxis.set_minor_locator(MultipleLocator(1))
			
			sub1.yaxis.set_major_locator(MultipleLocator(20))
			sub1.yaxis.set_minor_locator(MultipleLocator(10))
			#-------------------------------------------------
			
			plt.plot(x,y,label="H'F")
			plt.title(u'Gráfico_'+str(mes)+'_'+str(dia))
			plt.legend()
			plt.xlim(0,24)
			plt.ylim(160,360)
			plt.ylabel(u'Frequência (Hz)')
			plt.xlabel('Tempo(h)')
			plt.grid(True)
			
			#----------------salvar-------------------
			plt.savefig(u'Gráfico_'+str(mes)+'_'+str(dia)+'.png')
			plt.close()
			os.chdir(diretorio_inicial)#volta para principal...
			os.chdir('./entrada')#antes de começar proximo loop , volta para diretorio pasta entrada...

			
				
				
				
				
		
		


