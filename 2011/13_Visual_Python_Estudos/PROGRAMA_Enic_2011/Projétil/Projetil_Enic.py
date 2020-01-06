from visual import * #assim n preciso colocar vs ou visual... blabla

scene.x=150
scene.y=150

scene.width=800#largura
scene.height=600#altura

#scene.autoscale=0
scene.range=(100,110,100)
scene.center=(150,20,150)

ball=sphere(pos=(0,0,0),radius=2,material=materials.rough)#(0,2,0) fiz uma caixa com 2 de altura



ground=box(pos=(150,-1,0),size=(300,1,200),color=(0,0.5,0.5),material=materials.rough)
trajetoria=curve(color=color.red)



#-----------Dados----------------
x0=0
y0=0
t=0
dt= 0.01
#v0=25.63
v0=float(raw_input("Digite Valor da Velocidade Inicial \n"))
#angulo=34.15
angulo=float(raw_input("Digite Valor para Angulo de Lancamento \n"))
print "\n\n"
angulo=angulo*(pi/180) #degree
vx=v0*cos(angulo)
vy=v0*sin(angulo)


v_y=vy-9.8*t
v_x=vx


finished= True

vector1=arrow(pos=ball.pos,axis=vector(0,v_y/2,0),color=color.blue)
vector2=arrow(pos=ball.pos,axis=vector(v_x/2,0,0),color=color.blue)


while finished:
	rate(250)
	t=t+dt
	#posic eixo x (MRU) = x0+v*t  , v=vx
	alcance=x0+vx*t #ou seja ele vai aumentar , entao bola vai para --->
	#posic eixo x (MRUV) = y0+v*t-0.5*9.8*t^2
	altura= y0+vy*t-0.5*9.8*t**2
	
	
	
	#fazer variar o vetor em x e y...
	ball.pos=vector(alcance,altura,0)
	trajetoria.append(pos=ball.pos)
	
	
	
	
	if (t <= vy/9.8 and t >= vy/9.8 - dt):
		
	#if (t <= 1.47  and t >= 1.46) :
		#tempo para altura maxima = v0*sin(O)/g
		#print t , nao encontrei outra forma
		
		print "TEMPO PARA ALTURA MAXIMA \n"+str(t)
		
		raw_input("ALTURA MAXIMA \n"+str(ball.pos.y))
		
	
	
	if altura <=0:#quando altura for igual ou menor a 0 , perceba q esta dentro do loop , entao no primeiro zero ele n ira parar...
		
		alcance_max=alcance-(x0)
		
		print 'ALCANCE MAXIMO \n'+str(alcance_max)
		print 'TEMPO DE PERMANENCIA NO AR '+str(t)+'\n'
		finished=False
		
	v_y=vy-9.8*t
	v_x=vx
	
	vector1.pos=ball.pos
	vector1.axis.y=v_y/2
	
	vector2.pos=ball.pos
	vector2.axis.x=v_x/2
	
	
	
	