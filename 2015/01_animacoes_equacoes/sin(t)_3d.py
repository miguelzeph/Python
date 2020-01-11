#3D wave equation
import numpy as np
from numpy import pi,sin,cos,sqrt
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import matplotlib.animation as animation

x = np.arange(0,5,1)
y = np.arange(0,5,1)

X,Y = np.meshgrid(x,y)

#numero de ondas
kx=1
ky=1
#omega
w=1

#function
def u(x,y,t):
    return np.sin(w*t-kx*x-ky*y)


#Initial time
t0 = 0
#Time increment
dt = 0.5

#Building the datapoints
a = []
for i in range(100):
    z = u(X,Y,t0)
    t0 = t0 + dt
    a.append(z)


fig = plt.figure()
fig.set_dpi(100)
ax1 = fig.gca(projection='3d')

#Adding the colorbar 
#m = plt.cm.ScalarMappable(cmap=plt.cm.jet)
#m.set_array(a[0])
#cbar = plt.colorbar(m)



k = 0
def animar(i):
    global k
    Z = a[k]
    k += 1
    ax1.clear()
    ax1.plot_surface(X,Y,Z,rstride=1, cstride=1,cmap=plt.cm.jet,linewidth=0,antialiased=False)
    #ax1.contour(X,Y,Z)
    ax1.set_zlim(0,5)
    ax1.set_xlim(0,5)
    ax1.set_ylim(0,5)
    
anim = animation.FuncAnimation(fig,animar,frames=1000,interval=20)
plt.show()
