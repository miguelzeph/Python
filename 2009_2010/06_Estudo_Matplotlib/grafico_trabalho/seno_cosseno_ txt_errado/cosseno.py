# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np


x=np.arange(0,100,0.1)

y=np.cos(x)

plt.plot(x,y,'r*',5)

plt.show()