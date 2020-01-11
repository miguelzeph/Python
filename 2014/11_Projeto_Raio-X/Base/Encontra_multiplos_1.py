from __future__ import division
import numpy as np
import xlwt

n_pico = int(raw_input('Digite o numero de picos: \n'))

teta = []
for i in range(0,n_pico):
	teta.append((float(raw_input('Digite a posicao do pico \n'))*np.pi/180.00)/2.0)

	
	
#(Sin(tetaA)/Sin(tetaMin))^2

Valor = []

for i in range(0,n_pico):

	Valor.append(float(((np.sin(teta[i])**2)/(np.sin(teta[0])**2))))

tabela = {}
C = 20

for i in range(1,C):
	tabela[i]=[]
	for j in range(0,len(Valor)):
		
		final = Valor[j]*i
		
		arredondar = (float("%.2f"%(final)) - float("%.0f"%(final)))*100
		
		if arredondar >= 85:
		
			tabela[i].append(round(final))
			
		elif arredondar <= 10:
		
			tabela[i].append(round(final))
		
		else:
			
			tabela[i].append(final)
			
w = xlwt.Workbook()

sheet = w.add_sheet("Folha 1")

		
for i in range(1,C):
	for j in range(0,len(Valor)):
		sheet.write(j,i,tabela[i][j])

w.save('dados.xls')



	

	



	



