from visual import *

# tamanho do ecra
scene.width = 800
scene.height = 600

# parte do espaço 3D k mostra

#scene.autoscale = 0
scene.range = (300,200,100)
scene.center = (50,50,0)

valuesset = True

mylabel = label(pos=(100,100,0),text="velocity x: ",height=10)
mylabel.text = "velocity x: 0" + "\nvelocity y: 0 "

y=2
n = 0

#objectos
ball = sphere(pos=(0,4,0),radius=4, color=color.green,material=materials.earth) #uma bola
ground = box(pos=(50,-1,0),size=(1000,0.5,500),material=materials.wood) #o chao
canhao = box(pos=(-70,2,0),size=(10,5,7), color=color.red,material=materials.wood) #o canhao simbolico

#constantes e coiso
gravity = 9.8  # m/s**2

#user settings

if valuesset == true:
    velocity=input('Introduz um valor para a velocidade imprimida pelo "xuto" (m/s) :')
    angle=input('Introduz um valor para o angulo do "xuto" (graus) :')
    inicialalt=input('A que Altura do chão se dá o "xuto"? (m) : ')
    altlaicnh=inicialalt
    inicialalt= inicialalt + 4
    w=input('queres que a bola deixe uma trajectoria? y ou n : ')
    valuesset = false
    
#inicialalt=4
#angle = 50
#velocity = 20
satan =angle #pa no fim nao ter de converter pa graus outra bez
angle = angle * (pi/180) # convertido pa radianos

#ajustar altura inicial
canhao.pos.y = inicialalt
ball.pos.y = inicialalt

VelocityY = velocity * sin(angle)
VelocityX = velocity * cos(angle)

seconds = 0 
dt = .01 #incremento

if not valuesset:#se n for verdade (ou seja se valuesset = True ele n faz ... pois ele vira false , mais se ele virar false duas negacao torna-se verdadeiro ...)

    #loop do canhao
    disparou = False
    while not disparou:
        rate(100)
        seconds += dt
        canhaoX = -70 + velocity * seconds
        canhao.pos = vector(canhaoX,inicialalt,0) #pa mudar canhao de sitio no coiso 3D

        if canhao.pos.x >= 0: 
             disparou = True
             seconds = 0
             
        if w >= 1:
            ball.trail = curve(color=color.cyan)#rasto
        

    #loop da bola

    finished = False
    while not finished:
        rate(100) # nao correr mais de 100 vezes per sec
        seconds += dt 

        # y(t) = y0 + v0*t + .5 * a * t**2
        # v(t) = v0 + a * t
        ballY = inicialalt + VelocityY * seconds - .5 * gravity * seconds**2
        ballX = VelocityX * seconds
        v = VelocityY - gravity * seconds

        if VelocityX <=0.005:
            if VelocityX >= -0.005:
                VelocityX = 0

        ball.pos = vector(ballX,ballY,0) #pa mudar a bola de sitio no coiso 3D

        if w >= 1 :
            ball.trail.append(pos=ball.pos) #adicionar rast0

        if v >= 0: #se a velocidade for positiva
            alturamax = ballY #altura maxima é igual á altura a que a bola tá
            #ao deixar de ser positiva deixa de mudar e sabemos a altura atingida
        
        mylabel.text = "velocity x: " + str(VelocityX) + "\nvelocity y: " + str(v)


        velocidadesolo = - v
    
        if ballY - 4 <= 0: #o menos 4 é o raio da bola, senao fazia as contas para centro d bola
            finished = True #acaba o loop
            mylabel.text = "velocity x: 0" + "\nvelocity y: 0 " 
            if ballX <= 0.005: #obtinha valores estranhos sem isto tipo 3.12580771813e-014
                if ballX >= -0.005:
                    ballX = 0
            # agora diz estas tretas todas

            data = label(pos=(-70,80,0),text="data",height=10)
            data.text = "velocidade inicial: " + str(velocity) + "\nangulo lancamento: " + str(satan) + "\ntempo de voo: " + str(seconds) + "\ndistancia percorrida segundo X : " + str(ballX) + "\naltura maxima atingida : " + str(alturamax) + "\nvelocidade com que atingiu o solo segundo y : " +str(velocidadesolo)