# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np


x=np.arange(0,100,100)
t=np.arange(0,1000,01)

k=10
w=50


y=A*np.cos(k*x-w*t)


plt.plot(x,y,'ro',20)

plt.show()