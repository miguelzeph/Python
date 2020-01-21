#!/usr/bin/env python
#! -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np

arq=open("./tirei_erro.txt","r")
dados=arq.readlines()
arq.close()

x=[]
y=[]

for i in range(0,len(dados)):
	x.append(float(dados[i][0:5]))
	y.append(float(dados[i][6:12]))

plt.plot(x,y,'r-')

plt.savefig("./graf.png")

plt.show()

