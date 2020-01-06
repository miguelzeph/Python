#primeiro vc precisa criar uma func...

def y(x,a,b):
	return (a*x**2-b)
	
import scipy.integrate as si

# y tem 3 variaveis .. logo o args tem qe ter 2 ... e vai na ordem 

#exemplo 
args = (2,0) # fica ... y = 2*x - 0 .... a=2 e b = 0 na ordem

ini = 0
fim = 1

# da o valor da integral e do erro
print si.fixed_quad(y,ini,fim,args)#gaussiana quadrada
print si.quad(y,ini,fim,args)
#veja q temos dois metodos , cada um se enquadra melhgor para cada tipo de funcao
raw_input('pause')

