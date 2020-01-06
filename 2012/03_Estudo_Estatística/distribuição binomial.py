#!/usr/bin/env python
#! -*- coding: utf-8 -*-
from __future__ import division
import matplotlib.pyplot as plt

import numpy as np

import scipy as sp

#Formula P = n!/((n-k)!*k!)*p^(k)*(1-p)^(n-k)


k = np.arange(0,10)
p=1.0/6.0
n=10

def fat(a):
	
	fat=1
	for i in range(1,a+1):
	
		fat=fat*i
	return fat

Pvetor=[]

for i in k:
	P=(fat(n)/(fat(n-i)*fat(i)))*p**(i)*(1-p)**(n-i)
		
	Pvetor.append(P)

#Jogadinha para colocar intervalo de 1 em 1--------
from matplotlib.ticker import MultipleLocator
sub1=plt.subplot(1,1,1)

sub1.xaxis.set_major_locator(MultipleLocator(1))
sub1.xaxis.set_minor_locator(MultipleLocator(0.5))


#----------------------------------------------------
	

plt.title(u'Distribuição Binomial')
plt.ylabel(u'Probabilidade')
plt.xlabel('Eventos possiveis')



plt.xlim(0,10,)
	
plt.plot(k,Pvetor,'r--',k,Pvetor,'ro')
plt.grid()

plt.show()