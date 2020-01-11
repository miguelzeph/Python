from __future__ import division
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')
X = np.arange(-1.7, 1.7, 0.02)
Y = np.arange(-1.7, 1.7, 0.02)
X, Y = np.meshgrid(X, Y)

a = 2.546

Z = (1+4*np.cos(np.sqrt(3)*X*a/2.0)*np.cos(Y*a/2.0)+4*(np.cos(Y*a/2.0))**2)**(1.0/2.0)
G = -1*(1+4*np.cos(np.sqrt(3)*X*a/2.0)*np.cos(Y*a/2.0)+4*(np.cos(Y*a/2.0))**2)**(1.0/2.0)

#contornos
#cset = ax.contour(X, Y, Z,15, xdir = 'x')
#cset = ax.contour(X, Y, Z,15, ydir = 'y')
cset = ax.contour(X, Y, Z,100, zdir = 'y', offset =-0.2) #QUERO SOMENTE A DIRECAO Z COM OFFSET...
cset = ax.contour(X, Y, G,100, zdir = 'y', offset =-0.2)


#ax.set_zlim(-1.5, 1.5)

#ax.zaxis.set_major_locator(LinearLocator(10))
#ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

#fig.colorbar(surf, shrink=1, aspect=1)

plt.show()

