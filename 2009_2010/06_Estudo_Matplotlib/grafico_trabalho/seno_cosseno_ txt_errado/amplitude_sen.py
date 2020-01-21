# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np


x=np.arange(0,100,0.1)

y=5*np.cos(x)
y1=np.sin(x)
plt.plot(x,y,'r*',10)

plt.show()