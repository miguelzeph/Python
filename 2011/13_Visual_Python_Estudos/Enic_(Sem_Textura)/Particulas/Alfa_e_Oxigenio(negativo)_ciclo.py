from visual import *




scene.width = 800
scene.height = 600
scene.x = scene.y = 0
scene.background = color.white
scene.fov = 0.01
scene.range = 200e-15
xstart = scene.range.x



#Distancia de Colisao
b =500e-15  # start with 15e-15, then do 80e-15


particula_Alfa = (2,4) # alpha particle
particula_Oxigenio = (-8,16) # oxygen nucleus (coloquei negativo...)



#Dados_Basicos:
k = 9e9
q = 1.6e-19
massa_proton = 1.7e-27
raio_proton = 1.3e-15




# - xstart = pos ele vem da esquerda !!!
alfa = sphere(pos=(-xstart,b,0), color=color.red)
oxigenio = sphere(pos=(0,0,0), color=color.blue)


#DADOS_ALFA---------------------------------------------------
massa_alfa = particula_Alfa[1]*massa_proton
alfa.radius = (massa_alfa/massa_proton)**(1.0/3.0)*raio_proton
alfa_carga = particula_Alfa[0]*q
#ENERGIA Cinetica
Energia = 1e4*q
vetor_velocidade=2.*massa_alfa*Energia
alfa_vel = vector(sqrt(vetor_velocidade),0,0)
curva_alfa = curve(color=alfa.color)


#DADOS OXIGENIO-----------------------------------------------
massa_oxigenio = particula_Oxigenio[1]*massa_proton
oxigenio.radius = (massa_oxigenio/massa_proton)**(1.0/3.0)*raio_proton
oxigenio_carga = particula_Oxigenio[0]*q
oxigenio_vel = vector(0,0,0)
curva_oxigenio = curve(color=oxigenio.color)


dt = 5.*xstart/(mag(alfa_vel)/massa_alfa)/1e5
ptot = alfa_vel+oxigenio_vel
vcm = ptot/(massa_alfa+massa_oxigenio)

##alpha.p = alpha.p-alpha.mass*vcm
##target.p = target.p-target.mass*vcm

##scene.autoscale = 0

while True:
	#rate(5000)
	
	r12 = alfa.pos-oxigenio.pos
	
	
	#Forca de Coloumb + vetor_normal (unitario)
	F = (k*alfa_carga*oxigenio_carga/mag(r12)**2)*norm(r12)
    
	#interacoes entre velocidades-------
	
	#forca e mais pois ele vem da direita com vetor negativo !!!
	alfa_vel = alfa_vel + F*dt
	
	
	#forca e menos pois ele sofre a forca de atracao para lado negativo !!!
	oxigenio_vel = oxigenio_vel - F*dt
	#-----------------------------------
	
	# x = xo + v*t
	
	#Divide pela massa de cada elementro , pois na verdade temos momentos diferentes , e isto afeta a forca ...
	alfa.pos = alfa.pos + (alfa_vel/massa_alfa)*dt
	# x = xo + v*t
	oxigenio.pos = (0,0,0)
	
	curva_alfa.append(pos=alfa.pos)
	curva_oxigenio.append(pos=oxigenio.pos)
