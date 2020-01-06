from math import *
from Blender.Draw import *
from Blender import BGL, Window, Mesh, Scene

class Buttons:
	"""
	Classe com para armazenar os botões para que
	os valores possam ser usados por outras rotinas
	sem usar variáveis globais
	"""
	# Equação
	formula = Create('cos(x) - sin(3*x)')
	# Variação
	delta = Create(.1)
def interface():
	"""
	Função que desenha a interface
	"""
	# Pega o tamanho da janela
	x, y = Window.GetAreaSize()
	# Desenha caixa de texto
	# Parâmetros: rótulo, evento, x, y, largura, altura, valor inicial,
	# tamanho máximo do texto, tooltip
	Buttons.formula = String('Fórmula: ', 0, 10, y - 30, 300, 20,
	Buttons.formula.val, 300, 'Entre com uma expressão Python')
	# Desenha caixa de número
	# Parâmetros: rótulo, evento, x, y, largura, altura, valor inicial,
	# mínimo, máximo, tooltip
	Buttons.delta = Number('Delta: ', 0, 10, y - 60, 300, 20,
	Buttons.delta.val, .01, 1., 'Entre com a variação')
	# Desenha os botões
	# Parâmetros: texto do botão, evento, x, y, largura, altura, tooltip
	PushButton('Ok', 1, 10, y - 90, 100, 20, 'Aplica as mudanças')
	PushButton('Fim', 2, 10, y - 120, 100, 20, 'Termina o programa')
	# Comandos OpenGL através da BGL
	BGL.glClearColor(.7, .7, .6, 1)
	BGL.glClear(BGL.GL_COLOR_BUFFER_BIT)
def events(evt, val):
	"""
	Função que responde a eventos diversos,
	menos os gerados por botões
	"""
	# Os eventos das teclas estão definidas em Draw
	if evt == ESCKEY:
		# Termina o programa
		Exit()
def buttons(evt):
	"""
	Função que responde a eventos dos botões
	"""
	if evt == 2:
		Exit()
	elif evt == 1:
		gen3d()
def gen3d():
	# Cena 3D
	cena = Scene.GetCurrent()
	x = y = z = 0
	while x < 2 * pi:
		# Calcula os valores de z
		z = eval(Buttons.formula.val)
		# Cria uma esfera de 16 segmentos, 16 anéis e 0.1 BU de raio
		s = Mesh.Primitives.UVsphere(16, 16, .1)
		esfera = cena.objects.new(s, 'Mesh')
		# Transfere a esfera para o local calculado
		esfera.setLocation(x, y, z)
		# Próximo x
		x += Buttons.delta.val
		# Atualiza a cena
	cena.update()
if __name__ == '__main__':
	Register(interface, events, buttons)