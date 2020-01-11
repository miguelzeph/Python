#Apliquei a serie de Fourie para f(x) = x^2

import numpy as np
import matplotlib.pyplot as plt

g = []

x = np.arange(-10,10,0.01)
for k in x:
	p =0
	for n in range(1,2):
		p = p+(4/(n**2))*(-1)**(n)*np.cos(n*k)
	g.append(p+(np.pi**2)/3)

y = x**2

plt.plot(x,g,label= 'n=1')
plt.plot(x,y,'b--',label='f(x)=x^2')
plt.xlim(-10,10)
plt.ylim(0,10)
plt.legend()
plt.show()

