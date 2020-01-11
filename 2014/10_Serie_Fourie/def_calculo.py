#Apliquei a serie de Fourie para f(x) = x^2

import numpy as np
import matplotlib.pyplot as plt

def g(x0,n0):

	g = []
	
	x = np.arange(-x0,x0,0.0001)
	for k in x:
		p =0
		for n in range(1,n0):
			p = p+(4/(n**2))*(-1)**(n)*np.cos(n*k)
		g.append(p+(np.pi**2)/3)
		
	return x,g



plt.plot(g(10,5)[0],g(10,5)[1])
plt.xlim(-10,10)
plt.ylim(0,10)
plt.legend()
plt.show()


