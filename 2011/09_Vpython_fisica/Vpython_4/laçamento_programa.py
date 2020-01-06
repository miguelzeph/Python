#resumo: Qual a vantagem deste programa para o programa lacamento_2 ??? simples , vai na linha 64 e 73 
#onde estao os dois comandos que mudaram tudo , pois agora posso alterar vel, angulo de lancamento sem precisar
#dar o print e subs o valor , pois se n pega... 

#erro: unico erro e que quando o red cair primeiro ele nao ira esperar todas ficarem em altura = 0. 
#soluc: mas na versao acima , foi corrigido ...


from visual import * #assim n preciso colocar vs ou visual... blabla


# blue(azul) ->  coloquei nada...,green->verde , red->vermelho 
ball=sphere(pos=(-50,0,0),radius=2,color=color.blue)#(0,2,0) fiz uma caixa com 2 de altura
ballg=sphere(pos=(-50,0,0),radius=2,color=color.green)
ballr=sphere(pos=(-50,0,0),radius=2,color=color.red)



ground=box(pos=(0,-1,0),size=(250,1,10))


#-----------Dados----------------
seconds=0
g=0
r=0
dt= 0.01
v0=40
#---------------Bola azul-------
angulo=30
angulo=angulo*(pi/180)
vx=v0*cos(angulo)
vy=v0*sin(angulo)
#--------------Bola Verde ------
angulog=45
angulog=angulog*(pi/180)
vxg=v0*cos(angulog)
vyg=v0*sin(angulog)
#------------Bola vermelha------
angulor=80
angulor=angulor*(pi/180)
vxr=v0*cos(angulor)
vyr=v0*sin(angulor)

#---------------------------------------------
finished= False

while not finished:
	rate(100)
	seconds=seconds+dt
	g=g+dt
	r=r+dt
	
	#bola azul
	alcance=-50+vx*seconds
	altura= 0+vy*seconds-0.5*9.8*seconds**2
	ball.pos=vector(alcance,altura,0)
	
	#bola verde
	alcanceg=-50+vxg*g
	alturag= 0+vyg*g-0.5*9.8*g**2
	ballg.pos=vector(alcanceg,alturag,0)
	#bola vermelha
	alcancer=-50+vxr*r
	alturar= 0+vyr*r-0.5*9.8*r**2
	ballr.pos=vector(alcancer,alturar,0)
	if altura <=0:
		seconds=seconds-dt#unica jogada que achei , pois se n fosse assim eu teria de dar um print e achar valor depois chamar seconds = a tal... assim eu mantenho o seconds constante ate chegao fim o programa.
		
		#------------aqui em baixo esta a jogada ruin ...-------------
		#print seconds
		#seconds=3.43
		#--------------------------------------------------------------
		
		ball.pos=vector(alcance,0,0)
		
	if alturag <=0:
		g=g-dt #analogamente , irei manter constante....
		
		#--------------jogada ruim-----------------------------------
		#print g
		#g=4.85
		#------------------------------------------------------------
		
		ballg.pos=vector(alcanceg,0,0)
		
	if (altura <=0 and alturag <=0 and alturar <=0):#quando altura for igual ou menor a 0 , perceba q esta dentro do loop , entao no primeiro(comeco) zero ele n ira parar...
	#if alturar <=0:
		finished=True#vai brecar o loop
		#bola azul
		alcance_max=alcance-(-50)
		print 'alcance maximo da bola azul='+str(alcance_max)
		#bola verde
		alcance_max=alcanceg-(-50)
		print 'alcance maximo da bola verde='+str(alcance_max)
		#bola vermelha
		alcance_max=alcancer-(-50)
		print 'alcance maximo da bola vermelha='+str(alcance_max)
		
	