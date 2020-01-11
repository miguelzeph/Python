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

A=8.85e-12
e1_offset = 0
e2_offset = 0

e1 = (1/A)*(eo+(eo*(wp**(2.0))*((wo**(2.0))-(w**(2.0))))/(((wo**(2.0))-(w**(2.0)))**(2.0)+(gama*w)**(2.0)))+e1_offset

e2 = (1/A)*((eo*(wp**(2.0))*(gama*w))/(((wo**(2.0))-(w**(2.0)))**(2.0)+(gama*w)**(2.0)))+e2_offset

#e = ((e1)**(2.0)+(e2)**(2.0))**(1.0/2.0)

#-------GRAFICO1 - V ----------------------------------------
ax1=plt.subplot(121)
plt.subplots_adjust(left=0.1, bottom=0.3)
k, =plt.plot(w,e1,'b-',label="e'")

#copy;;;;
plt.xlabel('Frequencia(Hz)')
plt.ylabel("e'")
plt.ylim(-100,100)
plt.xlim(7e9,14e9)

plt.legend()
plt.grid(True)
#;;;;;

#-------GRAFICO2 - V ----------------------------------------
ax2=plt.subplot(122)
u, =plt.plot(w,e2,'r-',label='e"')

plt.xlabel('Frequencia(Hz)')
plt.ylabel('e"')
plt.ylim(-100,100)
plt.xlim(7e9,14e9)

plt.legend()
plt.grid(True)

#---------------------------------------------------------

#programa interacao****************************)))))))--------------------------------------------------
axcolor = (0.5,0.7,0.7)


gama_ = plt.axes([0.1, 0.15, 0.3, 0.03], axisbg=axcolor)
wo_ = plt.axes([0.1, 0.05, 0.3, 0.03], axisbg=axcolor)#(pos(x da barra),pos(y da barra),comprimento,largura)
wp_  = plt.axes([0.1, 0.10, 0.3, 0.03], axisbg=axcolor)

A_  = plt.axes([0.6, 0.15, 0.3, 0.03], axisbg=axcolor)
e1_ = plt.axes([0.6, 0.1, 0.3, 0.03], axisbg=axcolor)
e2_ = plt.axes([0.6, 0.05, 0.3, 0.03], axisbg=axcolor)#(pos(x da barra),pos(y da barra),comprimento,largura)




gamabar= Slider(gama_, 'Gama', 0, 1e10, valinit=gama)
wobar= Slider(wo_, 'wo', 8.2e6, 12.4e9, valinit=wo)
wpbar = Slider(wp_, 'wp', 8.2e9, 12.4e9, valinit= wp)

Abar= Slider(A_, 'A', -100, 100, valinit=A)
e1bar = Slider(e1_, 'e1', -100,100 , valinit=e1_offset)
e2bar = Slider(e2_, 'e2', -100, 100, valinit=e2_offset)


def update1(val):

	w = np.arange(ini,fim,inter)
	
	
	gama = gamabar.val
	wo = wobar.val
	wp = wpbar.val
	
	A = Abar.val
	e1_offset=e1bar.val
	e2_offset=e2bar.val
	
	e1 = (1/A)*(eo+(eo*(wp**(2.0))*((wo**(2.0))-(w**(2.0))))/(((wo**(2.0))-(w**(2.0)))**(2.0)+(gama*w)**(2.0)))+e1_offset
	e2 = (1/A)*((eo*(wp**(2.0))*(gama*w))/(((wo**(2.0))-(w**(2.0)))**(2.0)+(gama*w)**(2.0)))+e2_offset
	#e = ((e1)**(2.0)+(e2)**(2.0))**(1.0/2.0)
	
	k.set_ydata(e1)
	u.set_ydata(e2)
	#h.set_ydata(e)
	
	plt.draw()
	

gamabar.on_changed(update1)
wobar.on_changed(update1)
wpbar.on_changed(update1)

Abar.on_changed(update1)
e1bar.on_changed(update1)
e2bar.on_changed(update1)

'''
def update2(val):

	w = np.arange(ini,fim,inter)
	
	Abar= Abar.val
	gama = gamabar.val
	wo = wobar.val
	wp = wpbar.val
	
	
	e2 = A*((eo*(wp**(2.0))*(gama*w))/(((wo**(2.0))-(w**(2.0)))**(2.0)+(gama*w)**(2.0)))
	
	u.set_ydata(e2)
	
	plt.draw()

Abar.on_changed(update2)	
gamabar.on_changed(update2)
wobar.on_changed(update2)
wpbar.on_changed(update2)'''

plt.show()