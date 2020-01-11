from __future__ import division
import numpy as np

#onda - comprimento de onda do raio X(fixo)
onda=1.54032e-10
#a - parametro de rede do niquel (fixo)
#a= 3.507e-10 Calculado - estrutura CFC
a=10.6040e-10

#h,k,l - indices de miller (variar)



for l in range(0,6):
	for k in range(0,6):
		for h in range(0,6):
			try:
				d_inverso = ((h**2+k**2+l**2)/a**2)**(1.0/2.0)
				
				
				Angulo = np.arcsin((onda*d_inverso)/(2))*(180.0/np.pi)*2#esse x2 e devido Teta -> 2Teta (angulo de saida)
				
				print "Plano (",str(h),str(k),str(l),")\nAngulo = ",str(Angulo)
				raw_input()
			except ZeroDivisionError:
				print 'div por 0...'


