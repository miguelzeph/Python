from visual import * #assim n preciso colocar vs ou visual... blabla

scene.width=800#largura
scene.height=600#altura

scene.autoscale=0
scene.range=(100,100,100)
scene.center=(50,0,0)




puck=cylinder(pos=(0,0,0),axis=(0,2,0),radius=2,color=color.blue)
puck_mass= 10 #kg

ground=box(pos=(50,-1,0),size=(100,2,50))

#-----------Dados----------------
seconds=0
dt= 0.01
v0=30
angulo=30
angulo=angulo*(pi/180) #degree
vx=v0*cos(angulo)
vy=v0*sin(angulo)
vz=0



#---------Texto----------------------
Texto=label(pos=vector(0,40,0),text='...')
#--------------------------------------

#----------velocidade total-----------
vel_jogada=vector(vx,vy,vz)

vel_vento=vector(0,0,0)

vel_total= vel_jogada + vel_vento

#----------Velocidade y e x------
velocidadey=vel_total.y
velocidadex=vel_total.x



finished= False

while not finished:
	rate(100)
	seconds=seconds+dt
	

	
	#------------------------------------------------------------------------------------
	# X MRU
	#puck.x=vel_total.x*seconds (temos de colocar dentro do if e else , pois se n programa sera contrariado)
	# Y MRUV
	puck.y= 0+vel_total.y*seconds-0.5*9.8*seconds**2
	# Z MRU
	puck.z= vel_total.z*seconds
	# varia a posic....
	puck.pos=vector(puck.x,puck.y,puck.z)
	#-------------------------------------------------------------------------------------
		
	#---------------------Colocar o Atrito ---------------------------------------------#
	if puck.y <=0:
		puck.y=0
		#Force_atrito=Normal_Force*CoefficientKinetic
		Coefficient_of_kinetic=2
		
		Peso=puck_mass*9.8
		Normal_Force=Peso
		
		Force_friction=Normal_Force*Coefficient_of_kinetic
		
		#f=m.a --> a = f/m
		
		acceleration_friction=Force_friction/puck_mass
		
		#agora teremos uma aceleracao agindo ao oposto da velocidade no eixo x... 
		#obs: sinal e negativo pois age contrario a velocidade de x...
		velocidadex += -acceleration_friction*dt 
		
		puck.x= puck.pos.x +velocidadex*dt
		
	else:# se n estiver no chao , entao a velocidade e constante e continua sendo um MRU...
		
		puck.x=vel_total.x*seconds 
	
	#------------------velocidade Y  MRUV-----------------------------
	if puck.y !=0:
		velocidadey += - 9.8*dt
		#if (puck.y >0.0 and puck.y <0.2):#unico recurso que pensei ... e um valor aproximado da queda...
		#	velocidade_de_queda=velocidadey   fica lento d+...
				
	else:
		
		velocidadey=0
	
	
	#-------------------------Velocidade X constante ----------------------------#
	if velocidadex > 0:#quando velocidade em x for igual a zero , pare o programa.... facil
		velocidadex=velocidadex
	else:
		velocidadex=0
		finished = True
		
	
		
	#---------TEXTO-----------------------------------------------------------------------
	Texto.text='velocidade em x ='+str(velocidadex)+'\nvelocidade em y ='+str(velocidadey)
	#label(pos=vector(0,60,0),text='velocidade da queda'+str(velocidade_de_queda)) fica lento...
	#-------------------------------------------------------------------------------------
		
		
		
		