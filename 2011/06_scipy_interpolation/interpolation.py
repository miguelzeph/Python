import scipy.interpolate as si
import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0,100)

#y=np.random.randn(100)
y=np.sin(x)

plt.plot(x,y,'r--',label='sin')


#smoothing=si.UnivariateSpline(x,y[1,[1,2],3])
smoothing=si.UnivariateSpline(x,y)

xx=np.arange(0,100,0.01)
yy=smoothing(xx)
plt.plot(xx,yy,'bo',label='interpo')

plt.legend()
plt.show()