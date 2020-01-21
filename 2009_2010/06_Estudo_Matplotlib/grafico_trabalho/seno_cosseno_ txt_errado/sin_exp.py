# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np


x=np.arange(0,5,0.001)


A=np.exp(x)

y=A*np.cos(x)


plt.plot(x,y,'r-')

plt.show()