# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np


x=np.arange(0,100,0.1)

A=x

y=A*np.cos(x)


plt.plot(x,y,'r*')

plt.show()