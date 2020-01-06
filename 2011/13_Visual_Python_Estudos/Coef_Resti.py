from visual import *
from visual.controls import *

#constantes
g = 9.8
dt = 0.01

#lado da janela
lado = 350

#janela principal
display(x=0, y=0, width=lado, height=lado, range=(25,25,25), center=(0,10,0))
#janela dos controlos
c = controls(x=lado, y=0, width=lado, height=lado, range=60,
             title="coef. restituicao");

#inicializacao dos objectos
bola = sphere(pos=(0., 20., 0.), radius=2.0, color=color.red)
terra = box(pos=(0., -0.5, 0.), size=(20, 0.5, 20), color=color.blue)

#algumas propriedades da bola
bola.vel = vector(0.,-0.1, 0.)
bola.cr = 1

#evita o autoscale
scene.autoscale=0

#funcao que altera o coeficiente de restituicao
def setC_r(x):
    bola.cr=x.value

#reset da posicao da bola
def setPos():
    bola.pos.y = 20.
    bola.vel.y = 0.

#inicializacao do slider
s = slider(pos=(-15, 40), width=10, length=80, axis=(0,-1,0), min=0, max=1,
           action=lambda: setC_r(s))

#inicializacao do reset
b = button(pos=(25, 0), witdth=15, length=20, text="RESET", action=lambda: setPos()) 

#escolha do valor inicial do slider
s.value=1


while 1:
    #controla o rate do ciclo (deve ser usado com atencao ao dt
    rate(100)
    #procura interaccoes nos controlos
    c.interact()
    #actualiza a posicao
    bola.pos = bola.pos + bola.vel*dt

    #teste de colisao
    if bola.pos.y < bola.radius:
        bola.pos.y=bola.radius
        bola.vel.y = -bola.vel.y*bola.cr
    else:
        bola.vel.y = bola.vel.y -g*dt