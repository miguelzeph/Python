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

ini =1#e9
fim = 50#e9
inter = 0.1#e9


w_cria = np.arange(ini,fim,inter)

for i in range(0,len(w_cria)):
	
	w = w_cria[i]#/1e9
	


	Q = e1(7,10,3,w)+ e1(10,10,3,w)+e1(40,100,80,w)#falta somar +1
	R = e2(7,10,3,w)+ e2(10,10,3,w)+e2(40,100,80,w)
		
		
	E1.append(Q)
	E2.append(R)
	W.append(w)
	
plt.plot(W,E1,W,E2)

plt.show()
