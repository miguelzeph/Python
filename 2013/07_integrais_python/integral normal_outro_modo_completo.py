import scipy.integrate as si

k,h = 1,1#constantes

func = lambda x: k*x/h
a,b = 0,1

I = si.quad(func,a,b)
print I
print I[0]
raw_input()