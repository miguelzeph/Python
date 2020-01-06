import xlrd
import os

ods = xlrd.open_workbook('./dados.ods')
plan = ods.sheets()[0]


arq=open('./dados.txt','w')

#primeira linha ------------
linha = plan.row_values(0)
titulo="%s	%s\n"%(str(linha[0]),str(linha[1]))
arq.write(titulo)
#-----------------------------


for i in range (1,plan.nrows):
	
	linha = plan.row_values(i)#vetor
	
	data = str(linha[0])
	
	dados= float(linha[1])
	
	#programa trocar (,) --> (.)-------------
	#dados_novos = dados.replace(',','.')
	#--------------------------------------
	
	
	
	escrever='%s	%0.3f\n'%(data,dados)
	
	arq.write(escrever)

arq.close()