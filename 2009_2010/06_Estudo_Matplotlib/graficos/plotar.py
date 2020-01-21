import matplotlib.pyplot as plt
import numpy as np

x=np.arange(-np.pi,np.pi,0.1)
y=np.sin(x)
#grafico 1

plt.plot(x,y,'r-',x,x**2+2,'g^')
#plt.axis([-5.0,5.0,-1.5,1.5])
plt.title('Meu grafiquinho')
plt.xlabel('Valore de X')
plt.ylabel('Valore de Y')
plt.show()
#grafico 2
z=np.arange(-10,10,1.0)

plt.plot(z,z+1,'r-')
plt.show()

