# -*- coding: utf-8 -*-
import os

voltar=os.getcwd()#retornar o diretorio em forma de str, perceba quero o primeiro diretorio antes do loop
saida='./dados_agrupados/gama.txt'
arq_saida=open(saida,'w')
for numero in range(1,4):	
	os.chdir('./parte_'+str(numero))
	entrada='./saida/gama.txt'
	if os.path.exists(entrada):
		arq_entrada=open(entrada,'r')
		arq_dados=arq_entrada.readlines()
		arq_entrada.close()
		for linha in range(0,len(arq_dados)):
			arq_saida.write(arq_dados[linha])	
			os.chdir(voltar)
			#os.chdir('c:\\Documents and Settings\\Luiz Guilherme\\Desktop\\Trabalho_Gama_Novo\\2010\\2010_mes_07')
arq_saida.close()