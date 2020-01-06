import Blender
import math
import time

# Pega a cena atual
cena = Blender.Scene.GetCurrent()
# Elementos da cena "default"
camera = Blender.Object.Get()[0]
cubo = Blender.Object.Get()[1]
lamp = Blender.Object.Get()[2]
# Move a câmera
camera.setLocation(8., -8., 4.)
camera.setEuler(math.radians(70), 0.,math.radians(45))
# Muda a lente
camera.data.lens = 30
# Remove da cena o objeto "default"
cena.objects.unlink(cubo)
# Altera a intensidade da luz
lamp.data.energy = 1.2
# Muda o tipo para "Sun"
lamp.data.type = 1
# Aumenta o número de samples
lamp.data.raySamplesX = 16
lamp.data.raySamplesY = 16
# E a cor
lamp.data.col = 1., .9, .8
# Cria outra fonte de luz
lamp1 = Blender.Lamp.New('Lamp')
lamp1.energy = 0.5
lamp1.col = .9, 1., 1.
_lamp1 = Blender.Object.New('Lamp')
# Muda o lugar da fonte (default = 0.0, 0.0, 0.0)
_lamp1.setLocation(6., -6., 6.)
# "Prende" a fonte de luz na cena
_lamp1.link(lamp1)
cena.objects.link(_lamp1)
# Cria um material
material1 = Blender.Material.New('newMat1')
material1.rgbCol = [.38, .33, .28]
material1.setAlpha(1.)
# Cria uma textura
textura1 = Blender.Texture.Get()[0]
textura1.setType('Clouds')
textura1.noiseType = 'soft'
textura1.noiseBasis = Blender.Texture.Noise['VORONOICRACKLE']
# Coloca no material
material1.setTexture(0, textura1)
mtex1 = material1.getTextures()[0]
mtex1.col = .26, .22, .18
mtex1.mtNor = 1
mtex1.neg = True
mtex1.texco = Blender.Texture.TexCo['GLOB']
material1.mode += Blender.Material.Modes['RAYMIRROR']
material1.rayMirr = 0.2
material1.glossMir = 0.8
# Cria o piso
mesh = Blender.Mesh.Primitives.Plane(40.)
piso = cena.objects.new(mesh,'Mesh')
piso.setLocation(0., 0., .05)
# Rotaciona o piso
piso.setEuler(0., 0., math.radians(45))
# Coloca o material no piso
piso.setMaterials([material1])
piso.colbits = 1
# Cria outro material
material2 = Blender.Material.New('newMat2')
material2.rgbCol = [.77, .78, .79]
material2.setAlpha(1.)
material2.mode += Blender.Material.Modes['RAYMIRROR']
material2.rayMirr = 0.6
material2.glossMir = 0.4
# Coloca textura no outro material
material2.setTexture(0, textura1)
mtex2 = material2.getTextures()[0]
mtex2.col = .3, .3, .4
mtex2.mtNor = 1
mtex2.neg = True
mtex2.texco = Blender.Texture.TexCo['GLOB']
mat = [material2]
# Cria objetos na cena
def objeto(local, tam, mat, prim=Blender.Mesh.Primitives.Cube):
	mesh = prim()
	obj = cena.objects.new(mesh, 'Mesh')
	obj.setLocation(*local)
	obj.size = tam
	obj.setMaterials(mat)
	obj.colbits = 1
	return obj
def coluna(x=0., y=0., z=0., mat=mat):
	# Cilindro
	prim = Blender.Mesh.Primitives.Cylinder
	# Topo
	local = x, y, 2.5 + z
	tam = .25, .25, .1
	objeto(local, tam, mat)
	# Base
	local = x, y, 0. + z
	objeto(local, tam, mat)
	# Corpo
	for k in xrange(10):
		local = x, y, .25 * k + z
		tam = .2 - k / 200., .2 - k / 200., .25
		objeto(local, tam, mat, prim)
for i in xrange(16):
	# Primeira fileira
	coluna(i - 8., 8)
	# Segunda fileira
	coluna(-8., i - 8.)
	# Aqueduto
	local = -8., i - 8., 3.
	tam = .5, .5, .5
	objeto(local, tam, mat)
	local = i - 8., 8., 3.
	objeto(local, tam, mat)
	z = .25
# Cria colunas em cima do piso
for i in (-3, 3):
	for j in range(-2, 3):
		# Fileiras X
		coluna(i, j, z)
		# Fileiras Y
		coluna(j, i, z)
		# Cantos
	for j in (-3, 3):
		coluna(i, j, z)
		
# Cria escada
for i in xrange(8):
	local = 0., 0., i / 32. - .25
	tam = 3.3 + (8. - i) / 8., 3.3 + (8. - i) / 8., .25
	objeto(local, tam, mat)
# Cria teto
for i in xrange(35):
	local = 0., 0., 2.9 + i / 60.
	tam = 3.5 - i / 200., 3.5 * ( 1. - i / 35.), .1
	objeto(local, tam, mat)
# Pega o "mundo"
world = Blender.World.Get()[0]
# Modo "blend" no fundo
world.skytype = 1
# Atualiza a cena
cena.update()