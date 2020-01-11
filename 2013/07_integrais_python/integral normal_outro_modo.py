import scipy.integrate as si

func = lambda x: x
a,b = 0,1
I = si.quad(func,a,b)
print I