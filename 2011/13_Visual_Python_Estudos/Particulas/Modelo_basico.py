from visual import *

scene.background = color.white

p_beta = (1,0)
p_o=(8,16)

#Dados_Basicos:
k = 100
q = 1.6

b=50
scene.range = 100
xstart = scene.range.x



beta = sphere(pos=(-xstart,b,0),color=(0,0,1),radius=(p_beta[0]+1))
o = sphere(pos=(0,0,0),color=(1,0,0),radius=(p_o[0]+1))

E_cinetica_beta=340

beta_vel = vector(sqrt(E_cinetica_beta),0,0)

E_cinetica_o=0

o_vel = vector(sqrt(E_cinetica_o),0,0)



beta_carga=p_beta[0]*q
o_carga=p_o[0]*q


t = 0
dt = 0.0001


trajetoria1=curve(color=beta.color)
trajetoria2=curve(color=o.color)

while True:
	rate(200)
	
	r12 = beta.pos-o.pos
	
	t=t+dt
	
	#Forca de Coloumb + vetor_normal (unitario)
	F = (k*beta_carga*o_carga/mag(r12)**2)*norm(r12)
	
	#vetor_velocidade
	beta_vel=beta_vel-F
	
	#diviti pela massa , pois ele tem momento maior , apenas para diminuir a forca sobre o mais pesado
	o_vel =o_vel+F/(p_o[1])
	
	#posic , x = x0+v*t
	beta.pos = beta.pos  + beta_vel*t
	o.pos = o.pos + o_vel*t
	#o.pos = o.pos + F*t
	
	
	trajetoria1.append(beta.pos)
	trajetoria2.append(o.pos)
