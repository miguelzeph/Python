import matplotlib.pyplot as plt

import numpy as np

from mpl_toolkits.mplot3d import Axes3D

x=np.arange(-3,3,0.1)
y=x

[x,y]=np.meshgrid(x,y)

z=np.sqrt(x**2+y**2)

fig=plt.figure()
ax=Axes3D(fig)

ax.plot_surface(x,y,z)

plt.show()