import scipy.integrate as si

def I(x,k):
		
	return (x*k)# x vai ser integrado
#valor da constante k		
arg = (1)
#limite
a=0
b=1
#valor da integral
Q=si.quad(I,a,b,arg) #(funcao,limite inferior,limite superior,valor dos outros parametros)

print Q
raw_input()

#integral simples, tem q dar 0,5