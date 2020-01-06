import numpy as np
import matplotlib.pyplot as plt


y=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]

div=24.0

x=np.arange(0,len(y)/div,1/div) #escala nova em dias...

plt.plot(x,y)

plt.show()	