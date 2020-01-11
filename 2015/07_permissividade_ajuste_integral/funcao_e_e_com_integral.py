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
fim = 30#e9
inter = 0.1#e9


w_cria = np.arange(ini,fim,inter)

for i in range(0,len(w_cria)):
		
		
	wp = 10#8e8
	gama = 0.5#8e8
	w = w_cria[i]#/1e9
	a=10
	b=15
	args = (wp,gama,w)
		
	Q = si.quad(e1,a,b,args)
	R = si.quad(e2,a,b,args)
		
		
	E1.append(Q[0])
	E2.append(R[0])
	W.append(w)
	
plt.plot(W,E1,W,E2)

plt.show()
