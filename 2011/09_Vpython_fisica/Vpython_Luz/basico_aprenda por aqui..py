from visual import *
# Define posição inicial da câmera
scene.forward = (-0.1, -0.1, -0.1)
# Limpa a iluminação
scene.lights = []
# Define a iluminação ambiente
scene.ambient = (.1, .1, .2)


# Uma caixa de madeira
box(pos=(0,0,0),material=materials.wood)

lamp = frame(pos=(0, 1, 0))

c = (0.5, 0.5, 0.8)#RGB = Red, Green and Blue ... Max = 1 ..

local_light(frame=lamp, pos=(2, 1, 0), color=c)#função que cria a luz ...

sphere(frame=lamp, radius=0.1, pos=(2, 1, 0),
	color=c, material=materials.emissive) #fizemos está bola para representar o local da luz..

while True:
# Anima a lâmpada, rotacionando em torno do eixo Y
	lamp.rotate(axis=(0, 1, 0), angle=0.5)
	rate(20)