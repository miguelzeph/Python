# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np


x=np.arange(0,100,0.001)


A=5

y=A*np.cos(x)+A*np.sin(x)


plt.plot(x,y,'ro',20)

plt.show()