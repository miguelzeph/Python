import scipy.integrate as si

func = lambda x,y,z: x*y*z
x1,x2 = 0,1
y1,y2 = lambda x: 0, lambda x: 1
z1,z2 = lambda x,y: 0, lambda x,y:1
I = si.tplquad(func,x1,x2,y1,y2,z1,z2)
print I
raw_input()

#outra integral simples ... 1/8 = 0,125