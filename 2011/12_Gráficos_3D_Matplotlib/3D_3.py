import matplotlib.pyplot as plt
import scipy as sp
import numpy as np

from mpl_toolkits.mplot3d import Axes3D

x=sp.linspace(-3,3,300) # faz um vator de -3 ate 3 com 300 elementos.
y=x
#novo valor de x e y...
x,y=np.meshgrid(x,y)

z=(x**2+y**2)**2

fig=plt.figure()
ax=Axes3D(fig)

ax.plot_surface(x,y,z)

plt.show()