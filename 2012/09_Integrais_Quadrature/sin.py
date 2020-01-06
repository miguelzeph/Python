from scipy import integrate
import numpy as np
def myfunc(y,x,z):
	return np.sin(y)-x-z
 
# These are the arguments that will be passed as a and b to myfunc()
args = (0,0)
 
# Integrate myfunc() from 0.5 to 1.5
results = integrate.quadrature(myfunc, 0, np.pi/2, args)
print 'Integral = ', results[0], ' with error = ', results[1]