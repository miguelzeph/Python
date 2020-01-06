# coding: utf-8

import os
import xlwt

#------------arquivo de leitura ----------------
lista=os.listdir('.')
txts=[]

for i in range(0,len(lista)):
	if (lista[i].find('GAMMA') == -1):#find quando n?tem ele retorna -1
		continue
	else:
		txts.append(lista[i])
		
	y1=[]
	data1=[]
	for p in range(0,len(txts)):
			
		arq_entrada=open(txts[p],'r')
		arq_dados=arq_entrada.readlines()
		arq_entrada.close()
			
			
		y=[]
		data=[]		
		for linha in range(26,len(arq_dados)-1):
			
			dat=arq_dados[linha].split('\t')[2][0:5]
			dose=arq_dados[linha].split('\t')[6][0:5]
			
			if (float(dose) >= 0.25 and float(dose) <= 0.4):
				
				y.append(float(dose))
				data.append(dat)
				
			else:
				
				y.append(0.33)
				data.append(dat)
				
		y1.extend(y)#otima func, ela que add os valores ao novo vetor.
		data1.extend(data)
#----------------------------------------
		

#------- arquivo em calc ---------		
principal = xlwt.Workbook()

sheet = principal.add_sheet('dados',cell_overwrite_ok=True)

sheet.write(0,0,'Data')
sheet.write(0,1,'Dados')

for k in range (0,len(y1)):
	sheet.write(1+k,1,y1[k])# coloquei 1+k para nao subescrever
	sheet.write(1+k,0,data1[k])

principal.save('dados.ods')

#---------------------------------
	

