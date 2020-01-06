from scipy import integrate
def myfunc(y,x):
	return y-x
 
# These are the arguments that will be passed as a and b to myfunc()
args = (0)
 
# Integrate myfunc() from 0.5 to 1.5
results = integrate.quad(myfunc, 0, 1, args)
print 'Integral = ', results[0], ' with error = ', results[1]