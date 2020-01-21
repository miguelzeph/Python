# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np


x=np.arange(0,100,0.1)

y=np.cos(x)
y1=np.sin(x)
plt.plot(x,y,'r*',x,y1,'r+',10)

plt.show()