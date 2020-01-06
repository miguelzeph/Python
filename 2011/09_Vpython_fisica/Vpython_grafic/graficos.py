from visual.graph import *
# Gráfico de linha simples
g1 = gcurve(color=(.8, .6, .3))
# Gráfico de barras
g2 = gvbars(delta=0.02, color=(.6, .4, .6))
# Limites do eixo X do gráfico
for x in arange(0.0, 10.1, .1):
	# plot() recebe X e Y
	# Plotando a curva
	g1.plot(pos=(x, 2*sin(x)),color=color.blue)
	# Plotando as barras
	g2.plot(pos=(x,cos(x)),color=color.red)