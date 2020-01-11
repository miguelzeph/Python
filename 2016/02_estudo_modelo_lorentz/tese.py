from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as si
from matplotlib.widgets import Slider, Button, RadioButtons
#from matplotlib.ticker import MultipleLocator
import os



def e1(wo,wp,gama,w):
	return ((wp**(2.0))*((wo**(2.0))-(w**(2.0))))/(((wo**(2.0))-(w**(2.0)))**(2.0)+(gama**(2.0))*(w**(2.0)))

def e2(wo,wp,gama,w):
	return ((wp**(2.0))*(gama*w))/(((wo**(2.0))-(w**(2.0)))**(2.0)+(gama*w)**(2.0))


E1 =[]
E2 =[]
W=[]

ini =8#e9
fim = 12#e9
inter = 0.01#e9


w_cria = np.arange(ini,fim,inter)

for i in range(0,len(w_cria)):
	
	w = w_cria[i]#/1e9
	


	Q = e1(10,10,10,w) 
	R = e2(10,10,10,w)
		
		
	E1.append(Q)
	E2.append(R)
	W.append(w)
	


plt.plot(W,E1,'r-',linewidth=3,alpha=0.5,label="$\epsilon$'")
plt.plot(W,E2,'b-',linewidth=3,alpha=0.5,label='$\epsilon$"')

plt.figure(num=1,figsize=(15,10))

plt.legend()
plt.grid(True)

plt.xlabel('Freq(GHz)')

texto1='$\epsilon$"'
texto2="e  $\epsilon$' relativos"

plt.ylabel(texto1+texto2)


plt.savefig(u'Grafico.png')



plt.show()
