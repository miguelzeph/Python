# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np


x=np.arange(0,100,0.001)


A=5


y1=A*np.sin(x)
y2=A*np.sin(x+np.pi)#coloquei uma fase de 180º para poder anular com a onda y1 , assim temos uma onda destruitiva

y=y1+y2

plt.plot(x,y,'ro',x,y1,'r-',x,y2,'b-',20)


plt.show()