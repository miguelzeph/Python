from __future__ import division
import numpy as np

#Teste da funcao com valores aleatorios

f = np.arange(8.2e9,12.4e9,1e9)
lamb = 3e8/f #m

u = f*2.4/2e9#Modulo
e = f*2.4/7e9#Modulo

d = 0.0015#metros


z = abs(((u/e)**(1.0/2.0))*np.tanh(((2*np.pi*d/lamb)*((u/e)**(1.0/2.0)))*1j))

for i in range(0,len(z)):
	print z[i]


