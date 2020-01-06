from visual import *




scene.width = 800
scene.height = 600
scene.x = scene.y = 0
scene.background = color.white
scene.fov = 0.01
scene.range = 200e-15
xstart = scene.range.x



#Distancia de Colisao
b =15e-15  # start with 15e-15, then do 80e-15


particula_Alfa = (2,4) # alpha particle
particula_Oxigenio = (8,16) # oxygen nucleus
p_beta = (1,1)


#Dados_Basicos:
k = 9e9
q = 1.6e-19
massa_proton = 1.7e-27
raio_proton = 1.3e-15




# - xstart = pos ele vem da esquerda !!!
alfa = sphere(pos=(-xstart,b,0), color=color.red)
oxigenio = sphere(pos=(0,0,0), color=color.red)
beta= sphere(pos=(xstart,b,0),color=color.blue)

#DADOS_ALFA---------------------------------------------------
massa_alfa = particula_Alfa[1]*massa_proton
alfa.radius = (massa_alfa/massa_proton)**(1.0/3.0)*raio_proton
alfa_carga = particula_Alfa[0]*q
#ENERGIA Cinetica
Energia = 1e7*q
vetor_velocidade=2.*massa_alfa*Energia
alfa_vel = vector(sqrt(vetor_velocidade),0,0)
curva_alfa = curve(color=alfa.color)


#DADOS_Beta---------------------------------------------------
massa_beta = p_beta[1]*massa_proton
beta.radius = (massa_beta/massa_proton)**(1.0/3.0)*raio_proton
beta_carga = p_beta[0]*q
#ENERGIA Cinetica
Energia_b = 1e6*q
vetor_velocidade_b=2.*massa_beta*Energia_b
#esta do lado esquerdo , mais tem que ter velo indicando pelo lado negativo, por isto o menos
beta_vel = vector(-sqrt(vetor_velocidade_b),0,0)
curva_beta = curve(color=beta.color)


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
	#rate(10)
	
	r_a_o = alfa.pos-oxigenio.pos
	r_b_o = beta.pos-oxigenio.pos
	r_a_b = beta.pos-alfa.pos
	
	
	
	#Forca de Coloumb + vetor_normal (unitario)
	F_a_o = (k*alfa_carga*oxigenio_carga/mag(r_a_o)**2)*norm(r_a_o)
	F_b_o = (k*beta_carga*oxigenio_carga/mag(r_b_o)**2)*norm(r_b_o)
	F_a_b = (k*beta_carga*alfa_carga/mag(r_a_b)**2)*norm(r_a_b)
	
	
    
	
	#interacoes entre velocidades-------
	
	#forca e mais pois ele vem da direita com vetor negativo !!! (interac entre alfa e Oxi)
	#forca e menos (interac entre alfa e beta)
	
	alfa_vel = alfa_vel + F_a_o*dt - F_a_b*dt
	
	#analogo
	beta_vel = beta_vel - F_b_o*dt + F_a_b*dt
	
	
	#forca e menos pois ele sofre a forca de atracao para lado negativo !!!
	oxigenio_vel = oxigenio_vel - F_a_o*dt + F_b_o*dt
	#-----------------------------------
	
	#massa do beta e zero , tome cuidado... por isso do 1
	beta.pos = beta.pos + (beta_vel/massa_beta)*dt
	
	# x = xo + v*t
	alfa.pos = alfa.pos + (alfa_vel/massa_alfa)*dt
	# x = xo + v*t
	oxigenio.pos = oxigenio.pos + (oxigenio_vel/massa_oxigenio)*dt
	
	curva_alfa.append(pos=alfa.pos)
	curva_oxigenio.append(pos=oxigenio.pos)
	curva_beta.append(pos=beta.pos)
