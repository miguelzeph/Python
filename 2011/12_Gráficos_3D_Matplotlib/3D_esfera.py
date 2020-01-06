import matplotlib.pyplot as plt
import scipy as sp
import numpy as np

from mpl_toolkits.mplot3d import Axes3D

x=sp.linspace(-1.4,1.4,100) 
y=x
#novo valor de x e y...
x,y=np.meshgrid(x,y)

z=np.sqrt(4-x**2-y**2)

fig=plt.figure()
ax=Axes3D(fig)

ax.plot_surface(x,y,z)

plt.show()