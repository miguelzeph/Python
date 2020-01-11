from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as si
from matplotlib.widgets import Slider, Button, RadioButtons
#from matplotlib.ticker import MultipleLocator
import os


d = np.arange(0,10,0.25)

gama = 0.3
Vo = 1.0
Or = 30.0*np.pi/180
Zo = 50

V = (Vo*(1+abs(gama)**(2.0)+2*abs(gama)*np.cos(2*d-Or))**(1.0/2.0))
I = ((Vo/Zo)*(1+abs(gama)**(2.0)-2*abs(gama)*np.cos(2*d-Or))**(1.0/2.0))


#-------GRAFICO1 - V ----------------------------------------
ax1=plt.subplot(121)
plt.subplots_adjust(left=0.1, bottom=0.3)
k, =plt.plot(d,V,'b-',label='V')

#copy;;;;
plt.xlabel('d(m)')
plt.ylabel('V(V)')
#plt.ylim(0.0,1.1)

plt.legend()
plt.grid(True)
#;;;;;



ax2=plt.subplot(1,2,2)
u, =plt.plot(d,I,'g-',label='I')


#copy;;;;
plt.xlabel('d(m)')
plt.ylabel('I(A)')
#plt.ylim(0.0,1.1)

plt.legend()
plt.grid(True)
#copy;;;;

#---------------------------------------------------------

#programa interacao****************************)))))))--------------------------------------------------
axcolor=(0.5,0.7,0.7)

gama_ = plt.axes([0.1, 0.15, 0.3, 0.03], axisbg=axcolor)
Vo_ = plt.axes([0.1, 0.05, 0.3, 0.03], axisbg=axcolor)#(pos(x da barra),pos(y da barra),comprimento,largura)
Or_  = plt.axes([0.1, 0.10, 0.3, 0.03], axisbg=axcolor)
Zo_ = plt.axes([0.6, 0.15, 0.3, 0.03], axisbg=axcolor)


gamabar= Slider(gama_, 'Gama', 0, 1, valinit=0.5)
Vobar= Slider(Vo_, 'Voltagem', -5, 5, valinit=1)
Orbar = Slider(Or_, 'Phase', -10, 10, valinit= 30.0*np.pi/180 )
Zobar = Slider(Zo_, 'Zo', 0, 100, valinit=50)

def update1(val):

	d = np.arange(0,10,0.25)
	
	gama = gamabar.val
	Vo = Vobar.val
	Or = Orbar.val
	Zo = Zobar.val
	
	V = abs(Vo*(1+abs(gama)**(2.0)+2*abs(gama)*np.cos(2*d-Or))**(1.0/2.0))
	
	k.set_ydata(V)
	
	
	
	plt.draw()
	
gamabar.on_changed(update1)
Vobar.on_changed(update1)
Orbar.on_changed(update1)
Zobar.on_changed(update1)

def update2(val):

	d = np.arange(0,10,0.25)
	
	gama = gamabar.val
	Vo = Vobar.val
	Or = Orbar.val
	Zo = Zobar.val
	
	
	I = ((Vo/Zo)*(1+abs(gama)**(2.0)-2*abs(gama)*np.cos(2*d-Or))**(1.0/2.0))
	
	u.set_ydata(I)
	
	plt.draw()
	
gamabar.on_changed(update2)
Vobar.on_changed(update2)
Orbar.on_changed(update2)
Zobar.on_changed(update2)


plt.show()