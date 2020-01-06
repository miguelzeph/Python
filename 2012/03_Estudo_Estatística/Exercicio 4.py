#Lista 1 , exercicio 4

from __future__ import division
import numpy as np

d = [22.70,22.70,22.50,22.50,22.70,22.70,22.70,22.50,22.70,22.70]
#Teste --> print len(d) e len(l) , tem que ser 10...
l = [25.15,25.20,25.00,25.05,25.15,25.20,25.00,25.10,25.20,25.20]

#Media_Meu-----
def media(y):
	media=0
	for i in range(0,len(y)):
		media=y[i]+media
		
	media_final=(1.0/len(y))*media
	if y == d:
		print 'media do diametro= %f'%(media_final)
		return media_final
	if y == l:
		print 'media do comprimento= %f'%(media_final)
		return media_final

#-----------------------------------
print '\n'

#desvio_padrao_Meu-----
def desvio(y,ym):
	des=0
	for i in range(0,len(y)):
		
		des=(1.0/len(y))*(y[i]-ym)**(2.0)+des
	
	
	if y ==d:
		
		print "Desvio padrao Para o diametro"
	
	if y ==l:
		print "Desvio padrao para o Comprimento"
	
	#desvio padrao ao quadrado
	print des
	#desvio padrao 
	D=(des)**(1.0/2.0)
	print D
	#EM
	Em= D/(len(y)**(1.0/2.0))
	print Em
	print '\n'
	
desvio(d,media(d))
desvio(l,media(l))
#-----------------------Programa Feito pela Numpy-------
print "PROVA que a media esta certo"
md = np.mean(d)
print md
ld = np.mean(l)
print ld

print "\n"

print "PROVA que o desvio padrao esta certo"
print np.std(d)
print np.std(l)






		
		
		




