from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as si
from matplotlib.widgets import Slider, Button, RadioButtons
#from matplotlib.ticker import MultipleLocator
import os

ini =8.2e9
fim = 12.4e9
inter = 0.01e9

w = np.arange(ini,fim,inter)



eo= 8.85e-12
wo = 10e9 #variar
wp = 10e9 #variar
gama = 0.5#variar

e1 = eo+(eo*(wp**(2.0))*((wo**(2.0))-(w**(2.0))))/(((wo**(2.0))-(w**(2.0)))**(2.0)+(gama*w)**(2.0))

e2 = (eo*(wp**(2.0))*(gama*w))/(((wo**(2.0))-(w**(2.0)))**(2.0)+(gama*w)**(2.0))

e = ((e1)**(2.0)+(e2)**(2.0))**(1.0/2.0)

#-------GRAFICO1 - V ----------------------------------------
ax1=plt.subplot(221)
plt.subplots_adjust(left=0.1, bottom=0.3)
k, =plt.plot(w,e1,'b-',label="e'")

#copy;;;;
plt.xlabel('Frequencia(Hz)')
plt.ylabel("e'")
plt.ylim(-1e-9,10e-9)

plt.legend()
plt.grid(True)
#;;;;;


#-------GRAFICO2 - V ----------------------------------------
ax2=plt.subplot(223)
u, =plt.plot(w,e2,'g-',label='e"')


#copy;;;;
plt.xlabel('Frequencia(Hz)')
plt.ylabel('e"')
plt.ylim(-1e-15,30e-15)

plt.legend()
plt.grid(True)
#copy;;;;


#-------GRAFICO3 - V ----------------------------------------
ax3=plt.subplot(122)
h, =plt.plot(w,e,'r-',label='e')


#copy;;;;
plt.xlabel('Frequencia(Hz)')
plt.ylabel('e')
plt.ylim(-1e-8,10e-8)

plt.legend()
plt.grid(True)

#---------------------------------------------------------

#programa interacao****************************)))))))--------------------------------------------------
axcolor = (0.5,0.7,0.7)

gama_ = plt.axes([0.1, 0.15, 0.8, 0.03], axisbg=axcolor)
wo_ = plt.axes([0.1, 0.05, 0.8, 0.03], axisbg=axcolor)#(pos(x da barra),pos(y da barra),comprimento,largura)
wp_  = plt.axes([0.1, 0.10, 0.8, 0.03], axisbg=axcolor)



gamabar= Slider(gama_, 'Gama', 0, 1e6, valinit=gama)
wobar= Slider(wo_, 'wo', 8.2e9, 12.4e9, valinit=wo)
wpbar = Slider(wp_, 'wp', 8.2e9, 12.4e9, valinit= wp)


def update1(val):

	w = np.arange(ini,fim,inter)
	
	gama = gamabar.val
	wo = wobar.val
	wp = wpbar.val
	
	e1 = eo+(eo*(wp**(2.0))*((wo**(2.0))-(w**(2.0))))/(((wo**(2.0))-(w**(2.0)))**(2.0)+(gama*w)**(2.0))
	e2 = (eo*(wp**(2.0))*(gama*w))/(((wo**(2.0))-(w**(2.0)))**(2.0)+(gama*w)**(2.0))
	e = ((e1)**(2.0)+(e2)**(2.0))**(1.0/2.0)
	
	k.set_ydata(e1)
	u.set_ydata(e2)
	h.set_ydata(e)
	
	plt.draw()
	
gamabar.on_changed(update1)
wobar.on_changed(update1)
wpbar.on_changed(update1)


'''def update2(val):

	w = np.arange(ini,fim,inter)
	
	gama = gamabar.val
	wo = wobar.val
	wp = wpbar.val
	
	
	e2 = (eo*(wp**(2.0))*(gama*w))/(((wo**(2.0))-(w**(2.0)))**(2.0)+(gama*w)**(2.0))
	
	u.set_ydata(e2)
	
	plt.draw()
	
gamabar.on_changed(update2)
wobar.on_changed(update2)
wpbar.on_changed(update2)

def update3(val):

	w = np.arange(ini,fim,inter)
	
	gama = gamabar.val
	wo = wobar.val
	wp = wpbar.val
	
	
	e = ((e1)**(2.0)+(e2)**(2.0))**(1.0/2.0)
	
	
	h.set_ydata(e)
	
	plt.draw()
	
gamabar.on_changed(update3)
wobar.on_changed(update3)
wpbar.on_changed(update3)'''

plt.show()