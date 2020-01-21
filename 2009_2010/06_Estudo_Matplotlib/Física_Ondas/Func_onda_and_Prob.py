# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

L=2*np.pi
x=np.arange(0,L,0.01)
y=(2/(L))*np.sin(4*np.pi/(L)*x)

y1=(y)**2

x1=np.arange(0,9)
y2=(x1)*0

plt.plot(x,y,'b-',x1,y2,'black',lw=2)
plt.fill(x,y1,'g')


plt.xlabel('comprimento da caixa')
plt.ylabel('Func de Onda')
plt.title("Grafico Exercicio Tipler 6-20")
plt.xlim(0,L)
plt.grid()
plt.text(1,0.35,'Area Verde = Probabilidade de Encontrar Particula',bbox={'facecolor':'green', 'alpha':0.2, 'pad':20})
plt.annotate('Func de Onda',xytext=(4, -0.3),
xy=(3, -0.1),arrowprops=dict(facecolor='black', shrink=0.1),bbox={'facecolor':'Blue', 'alpha':0.2, 'pad':20})

plt.show()