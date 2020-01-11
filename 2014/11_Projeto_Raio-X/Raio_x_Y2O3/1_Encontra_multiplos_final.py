from __future__ import division
import numpy as np
import xlwt


teta2 = [20.50,29.16,33.75,35.91,39.83,43.49,48.51,53.18,56.18,57.64,59.04,60.43]
teta = []

for i in range(0,len(teta2)):
	teta.append(((teta2[i]*np.pi/180.00)/2.0))


#(Sin(tetaA)/Sin(tetaMin))^2

Valor = []

for i in range(0,len(teta)):

	Valor.append(float(((np.sin(teta[i])**2)/(np.sin(teta[0])**2))))

tabela = {}
C = 20

for i in range(1,C):
	tabela[i]=[]
	for j in range(0,len(Valor)):
		
		final = Valor[j]*i
		
		arredondar = (float("%.2f"%(final)) - float("%.0f"%(final)))*100
		
		if arredondar >= 95:
		
			tabela[i].append(round(final))
			
		elif arredondar <= 5:
		
			tabela[i].append(round(final))
		
		else:
			
			tabela[i].append(final)
			
w = xlwt.Workbook()

sheet = w.add_sheet("Folha 1")

		
for i in range(1,C):
	for j in range(0,len(Valor)):
		sheet.write(j,i,tabela[i][j])

w.save('1_multiplos.xls')



	

	



	



