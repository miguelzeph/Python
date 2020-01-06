# -*- coding: utf-8 -*-
import os

os.chdir('./entrada')
lista=os.listdir('./')

for i in range(0,len(lista)):
	vetor=lista[i].split('_')
	novo_nome = vetor[0]+'_'+vetor[1]+'_'+vetor[2]+'_'+vetor[3]+'.txt'
	os.rename(lista[i],novo_nome)
		