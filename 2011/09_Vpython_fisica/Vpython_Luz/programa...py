from visual import *
# Define posição inicial da câmera
scene.forward = (-0.1, -0.1, -0.1)
# Limpa a iluminação
scene.lights = []
# Define a iluminação ambiente
scene.ambient = (.1, .1, .2)
# Uma caixa de madeira
box(material=materials.wood)
# Uma esfera de material semi-transparente
sphere(radius=.2, pos=(-1, -0.3, 1), color=(.4, .5, .4),
	material=materials.rough, opacity=.5)
# Uma textura xadrez
x = 2 * (2 * (1, 0), 2 * (0, 1))
# Define a textura nova
mat = materials.texture(data=x, interpolate=False,
	mapping='rectangular')
# Caixa com a nova textura
box(axis=(0, 1, 0), size=(4, 4, 4), pos=(0, -3, 0), material=mat)
# A lâmpada é um frame composto por uma esfera e uma fonte de luz
c = (1., .9, .8)
lamp = frame(pos=(0, 1, 0))
# Define uma fonte de luz
local_light(frame=lamp, pos=(2, 1, 0), color=c)
# Define uma esfera com material emissor
sphere(frame=lamp, radius=0.1, pos=(2, 1, 0),
	color=c, material=materials.emissive)
while True:
# Anima a lâmpada, rotacionando em torno do eixo Y
	lamp.rotate(axis=(0, 1, 0), angle=.1)
	rate(100)