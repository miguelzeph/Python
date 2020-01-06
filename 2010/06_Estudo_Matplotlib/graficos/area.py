# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np


x=np.arange(0,100,0.0001)

A=x

y=A*np.cos(x)


plt.fill(x,y,'r')

plt.show()