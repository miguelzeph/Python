# -*- coding: windows-1252 -*-
import os
for i in range(0,13):
	os.system("move *09_0"+str(i)+"*.txt c:\\\"Documents and Settings\"\\\"Luiz Guilherme\"\\Desktop\\Trabalho_Inacio\\Dados_Inacio\\Geiger\\2009\\Geiger_1_mes"+str(i))
	if i > 9:
		os.system("move *09_"+str(i)+"*.txt c:\\\"Documents and Settings\"\\\"Luiz Guilherme\"\\Desktop\\Trabalho_Inacio\\Dados_Inacio\\Geiger\\2009\\Geiger_1_mes"+str(i))
		continue
		