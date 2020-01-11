from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

g = []

x = np.arange(-3*np.pi,3*np.pi,0.01)

N= []
#SOMENTE NUMEROS IMPARES
for i in range(0,4):

	if i%2 == 0:
		continue
	else:
		N.append(i)
		


for k in x:
	p =0
	for n in N:
		p = p+(4/np.pi)*((1/n)*np.sin(n*k))
	g.append(p)


plt.plot(x,g,label= 'n=3')

plt.xlim(-10,10)
plt.ylim(-1.5,1.5)
plt.legend()
plt.show()

