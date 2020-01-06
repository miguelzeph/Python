
from visual import *

scene2 = display(background=(1,1,1))

coords = (-3, 3)

cor1 = (0.5, 0, 0)

cor2 = (0, 0.5, 0)

quadro = frame(pos=(0,0,0))

for x in coords:
	for y in coords:
		for z in coords:
		
			visual.sphere(frame = quadro,pos=(x, y, z), color=cor1,material=materials.emissive)

# Desenha os cilindros das arestas
for x in coords:
	for z in coords:
	# pos é a posição do centro da base do cilindro
	# radius é o raio da base do cilindro
	# axis é o eixo do cilindro
		visual.helix(frame = quadro,pos=(x, 3, z), color=cor2,
			radius=0.5,coils=20,thickness=0.1,axis=(0, -6, 0))
			
			#visual.helix(pos=(x,3,z), axis=(0,1,0), radius=0.5,coils=10,thickness=0.1,color=cor2)
	for y in coords:
		visual.helix(frame = quadro,pos=(x, y, 3), color=cor2,
			radius=0.5,coils=20,thickness=0.1,axis=(0, 0, -6))
for y in coords:
	for z in coords:
		visual.helix(frame = quadro,pos=(3, y, z), color=cor2,
			radius=0.5,coils=20,thickness=0.1,axis=(-6, 0, 0))


while True : 
	rate(45)
	quadro.rotate(axis = (0,1,0), angle= 0.01)
	quadro.rotate(axis = (1,0,0), angle= 0.001)
	quadro.rotate(axis = (0,0,1), angle= 0.02)