# -*- coding: utf-8 -*-

import os
import numpy as np
import matplotlib.pyplot as plt

arq_saida=open('./dados.txt','w')

numero=np.arange(0,10*np.pi,np.pi/2)

for i in range(0,len(numero)):
	x=i
	y=numero[i]
	
	linha="%0.2d %5.4f\n" %(x,y)
	
	arq_saida.write(linha)
arq_saida.close()