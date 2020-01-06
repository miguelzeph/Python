# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np


x=np.arange(0,100,0.001)

B=5
A=10
#ambos estão em faze, logo temos onda construtiva
y=A*np.cos(x)+B*np.cos(x)
y1=A*np.cos(x)
y2=B*np.cos(x)

plt.plot(x,y,'r-',x,y1,'r-',x,y2,'b-',20)

plt.show()