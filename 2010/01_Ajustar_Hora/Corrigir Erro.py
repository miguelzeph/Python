#!/usr/bin/python
# coding: utf-8

arquivo_velho = open('./entrada/Horas.txt','r')

leitura= arquivo_velho.readlines()

total_linha= len(leitura)

arquivo_velho.close()

arquivo_novo = open('./saida/Horas_Ajustadas.txt','w')


for i in range (1,total_linha):
	hora_dec= float(leitura[i])
	hora = int(hora_dec)
	min = float(hora_dec-hora)*60
	hora_min = float(hora+min/100)
	arquivo_novo.write(str(hora_min)+'\n')
arquivo_novo.close()