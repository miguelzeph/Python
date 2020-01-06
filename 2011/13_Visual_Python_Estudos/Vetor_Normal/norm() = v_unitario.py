from visual import *


#mag = magnitude , comprimento , modulo = raiz(x^2+y^2+z^2) = (x**2+y**2+z**2)**(1.0/2.0)
#norma() = unitario = V/|V|


v = (1,1,1)

#idem a mag(v)
modulo_v=sqrt(v[0]**2+v[1]**2+v[2]**2)

#idem a u = v/mag(v)
u = v/modulo_v

#Percebeu que nao deu certo .... so dara certo se eu colocar v =vector(1,1,1) , pois e uma func especial 
# da visual para dividir cada valor de um vetor ...