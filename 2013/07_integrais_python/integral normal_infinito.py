import scipy.integrate as si
import numpy as np
def I(x,k):
		
	return (x*k)# x vai ser integrado
#valor da constante k		
arg = (1)
#limite
a=0
b=1
#valor da integral
Q=si.quad(I,-np.inf,np.inf,arg) #(funcao,limite inferior,limite superior,valor dos outros parametros)

print Q
raw_input()

