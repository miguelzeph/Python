# -*- coding: utf-8 -*-


def media(y):
	media=0
	for i in range(0,len(y)):
		media=y[i]+media
		
	media_final=(1.0/len(y))*media
	
	return media_final

def desvio(y,ym):
	des=0
	for i in range(0,len(y)):
		
		des=(1.0/len(y))*(y[i]-ym)**(2.0)+des
	
	#desvio padrao ao quadrado = des
	#desvio padrao = D
	D=(des)**(1.0/2.0)

	return D
#qui-quadrado	
def X(y,yteorico,d):

	x = 0
	
	for i in range(0,len(y)):
		
		x = ((y[i]-yteorico[i])**(2.0))/((d[i])**(2.0)) + x
		
	return x
	
#qui-quadrado-reduzido
def Xred(y,v):

	xr=y/v
	
	return xr

