from pylab import *

X = np.arange(-1.9, 1.9, 0.03)
Y = np.arange(-1.9, 1.9, 0.03)
X, Y = np.meshgrid(X, Y)

Z = (1+4*np.cos(np.sqrt(3)*X*2.456/2.0)*np.cos(Y*2.456/2.0)+4*(np.cos(Y*2.456/2.0))**2)**(1.0/2.0)



#PLOTAR CONTORNOS-----------------------------------------
ext = [-1,1,-1,1]
imshow(Z,extent = ext)
contour(Z,15,colors = 'black',linewidths = 3,extent = ext)
#ESTE numero 15 e o valor de linhas que quero colocar...
#----------------------------------------------------------


#Desenhar a Primeira Zona de Brillouin---------------------
kx = [0.00,-0.77,-0.77,0.00,0.8,0.8,0.00]
ky = [-0.9,-0.43,0.48,0.92,0.48,-0.43,-0.9]

plot(kx,ky,color = 'black',linewidth = 3)
#----------------------------------------------------------

#Escrever--------------------------------------------------
cor = 'white'

text(0.02,-0.88,"K",fontsize = 20,color=cor)
text(-0.75,-0.43,"K'",fontsize = 20,color=cor)
text(-0.75,0.48,"K",fontsize = 20,color=cor)
text(0.02,0.92,"K'",fontsize = 20,color=cor)
text(0.8,0.48,"K",fontsize = 20,color=cor)
text(0.8,-0.43,"K'",fontsize = 20,color=cor)
#----------------------------------------------------------

xlabel('Kx')
ylabel('Ky')
title('Primeira Zona Brillouin Grafite')
#savefig('graf.png')
show()
