#2D wave equation
import numpy as np
from numpy import pi
import matplotlib.pyplot as plt
import matplotlib.animation as animation

x = np.arange(-pi,pi,0.1)

#numero de ondas
kx=3

#omega
w=1

#atenuacao
alfa = -0.4

#function
def u(X,t):
    return (-.5*np.exp(alfa*X)*np.sin(w*t-kx*X))


#Initial time
t0 = 0
#Time increment
dt = 0.25

#Building the datapoints
a = []
for i in range(100):
    valor = u(x,t0)
    t0 = t0 + dt
    a.append(valor)


fig = plt.figure()
fig.set_dpi(80)
ax1 = fig.add_subplot(1,1,1)

k = 0
def animar(i):
    global k
    y = a[k]
    k += 1
	
    ax1.clear()
    plt.plot(x,y)
    plt.ylim(-2,2)
    plt.xlim(-pi,pi)
    
    
anim = animation.FuncAnimation(fig,animar,frames=100,interval=20)
plt.show()
