from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(14,6))

#x,y = ogrid[-5:5:0.01,-5:5:0.01]

X = np.arange(-1.9, 1.9, 0.1)
Y = np.arange(-1.9, 1.9, 0.1)
X, Y = np.meshgrid(X, Y)
Z = (1+4*np.cos(np.sqrt(3)*X*2.456/2.0)*np.cos(Y*2.456/2.0)+4*(np.cos(Y*2.456/2.0))**2)**(1.0/2.0)

ax = fig.add_subplot(1, 2, 1, projection='3d')

p = ax.plot_surface(X, Y, Z, rstride=4, cstride=4, linewidth=0)


ax = fig.add_subplot(1, 2, 2, projection='3d')
p = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
cb = fig.colorbar(p, shrink=0.5)