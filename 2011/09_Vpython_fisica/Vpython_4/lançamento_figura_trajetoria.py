from visual import * #assim n preciso colocar vs ou visual... blabla

#scene.width=800#largura
#scene.height=600#altura

#scene.autoscale=0
#scene.range=(100,100,100)
#scene.center=(0,40,0)

ball=sphere(pos=(-50,0,0),radius=2,color=color.blue)#(0,2,0) fiz uma caixa com 2 de altura
ground=box(pos=(0,-1,0),size=(100,1,10))

#-----------Dados----------------
seconds=0
dt= 0.15 #aumentei o dt , para separar a distancia das posic das bolas...
v0=33.6
angulo=30
angulo=angulo*(pi/180) #degree
vx=v0*cos(angulo)
vy=v0*sin(angulo)
#---------------------------------


finished= False

while not finished:
	rate(50)
	
	seconds=seconds+dt
	#posic eixo x (MRU) = x0+v*t  , v=vx
	alcance=-50+vx*seconds #ou seja ele vai aumentar , entao bola vai para --->
	#posic eixo x (MRUV) = y0+v*t-0.5*9.8*t^2
	altura= 0+vy*seconds-0.5*9.8*seconds**2
	posic=vector(alcance,altura,0)
	#fazer variar o vetor em x e y...
	sphere(pos=posic,radius=2,color=color.blue)
	
	
	if altura <=0:#quando altura for igual ou menor a 0 , perceba q esta dentro do loop , entao no primeiro zero ele n ira parar...
		print 'o alcance max e este , ele da um valor de aprox 49 , mas lembre-se que ele saiu de -50 , logo ele parou no eixo x do grafico +50 , entao para achar comprimento e facil...basta fazer final - inicial , logo deslocamen NO GRAFICO foi de :'+str(alcance)
		alcance_max=alcance-(-50)
		finished=True#parar o loop
		print 'alcance maximo='+str(alcance_max)