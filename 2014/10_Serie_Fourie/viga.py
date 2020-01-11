from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

g = []

L =1
q = 1
E = 1
I = 1

N = []
for i in range(0,2):
	if i%2==0:
		continue
	else:
		N.append(i)

x = np.arange(0,L,0.01)
for k in x:
	p =0
	for n in N:
		p = p+((4*q*(L**4)/(E*L*np.pi**5))*(1/n**5)*np.sin(n*np.pi*k/L))
	g.append(p)


plt.plot(x,g,label= 'n=1')

plt.xlim(0,L)
plt.ylim(0,1)
plt.legend()
plt.show()

