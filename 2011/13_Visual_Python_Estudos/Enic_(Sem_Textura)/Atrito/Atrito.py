from visual import * #assim n preciso colocar vs ou visual... blabla
from visual.graph import *
from visual.controls import *

scene.x=0
scene.y=100

scene.width=500#largura
scene.height=500#altura

scene.autoscale=0
scene.range=(100,1000,1000)
scene.center=(100,60,100)

#grafico....
graph1 = gdisplay(x=0, y=0, width=250,height=250, 
          title='V(m/s)', xtitle='t(s)', ytitle='V(t)', 
          xmax=10, xmin=0., ymax=100, ymin=-50, 
          foreground=color.white, background=color.black)
		  
funcao1 = gcurve(color=color.blue)
funcao2 = gcurve(color=color.red)



	

puck=cylinder(pos=(0,0,0),axis=(0,5,0),radius=5,color=color.blue)
puck_mass= 10 #kg

#ground=box(pos=(200,-1,0),size=(400,2,100),material=materials.wood)
ground=box(pos=(200,-1,0),size=(400,2,100),color=(0.8,0.5,0.2))

vector1=arrow(pos=puck.pos,axis=vector(0,0,0),color=color.red)
vector2=arrow(pos=puck.pos,axis=vector(0,0,0),color=color.red)
vector3=arrow(pos=puck.pos,axis=vector(0,0,0),color=color.yellow)



#controle--------------------------

c = controls(x=250, y=0, width=250, height=250, range=60,title="Reset")
#display(x=0, y=0, width=lado, height=lado, range=(25,25,25), center=(0,10,0))
def settime():
	
	menu()
b = button(pos=(0, 0), witdth=15, length=20, text="RESET", action=lambda: settime()) 


def menu():
	#-----------Dados----------------
	seconds=0
	dt= 0.01
	v0=int(raw_input('VELOCIDADE INICIAL: '))
	angulo=int(raw_input("ANGULO INICIAL: "))
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
		rate(200)
		
		
		v_y = vy - 9.8*seconds
		v_x = vx
		
		seconds=seconds+dt
		
		funcao1.plot(pos=(seconds,velocidadex))#Energia Cinetica
		funcao2.plot(pos=(seconds,velocidadey))
		
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
		
			
		
		if puck.y <= 0:
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
			
			vector3.axis.x=-acceleration_friction
			
			
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
		
		
		
		vector1.pos=puck.pos
		vector1.axis.y=v_y/1.4
		vector2.pos=puck.pos
		vector2.axis.x=velocidadex/1.4
		vector3.pos=puck.pos
		
		if velocidadex <= 0:
			vector3.pos=(0,0,0)
			vector3.axis.x=0
			
		
		
		
		
		c.interact()
		
menu()		