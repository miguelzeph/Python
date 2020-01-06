#!/usr/bin/env python
#! -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import matplotlib.cm as cm
import matplotlib.image as mimg
import numpy as np

#paper_width=297.0
#paper_height=210.0
paper_width=200.0
paper_height=200.0
axes_linewidth=2
axes_label_paddding=10.0
axes_label_fontsize=14
major_ticks_size=15
minor_ticks_size=8
x_min=-83.0
x_max=-30.0
x_major_step=10.0
x_minor_step=2.0
y_min=-37.0
y_max=27.0
y_major_step=10.0
y_minor_step=2.0

plt.rcParams["axes.linewidth"]=axes_linewidth
plt.rcParams["xtick.major.size"]=major_ticks_size
plt.rcParams["xtick.minor.size"]=minor_ticks_size
plt.rcParams["ytick.major.size"]=major_ticks_size
plt.rcParams["ytick.minor.size"]=minor_ticks_size
plt.rcParams["xtick.major.pad"]=axes_label_paddding
plt.rcParams["xtick.minor.pad"]=axes_label_paddding
plt.rcParams["ytick.major.pad"]=axes_label_paddding
plt.rcParams["ytick.minor.pad"]=axes_label_paddding
plt.rcParams["xtick.labelsize"]=axes_label_fontsize
plt.rcParams["ytick.labelsize"]=axes_label_fontsize
plt.rcParams["lines.markeredgewidth"]=axes_linewidth
plt.rcParams["savefig.dpi"]=100

eq_file=open('./dipeq.dat','r')
eq_data=eq_file.readlines()
eq_file.close()

x_dipeq=[]
y_dipeq=[]

for i in range(1,len(eq_data)):
	x_dipeq.append(float(eq_data[i].split('\t')[0]))
	y_dipeq.append(float(eq_data[i].split('\t')[1]))

image=mimg.imread("./mapa.png")
image2=[]

w=1059 #422
h=1281 #440
for i in range(0,h):
	image2.append([])
	for j in range(0,w):
		image2[i].append(None)

for i in range(0,h):
	for j in range(0,w):
		image2[(h-1)-i][j]=image[i][j]

for hh in range(0,25):
	print hh
	if (hh < 10):
		entrada='./entrada/mtec02_284_0'+str(hh)+'.dat'
		saida='./saida/mtec02_284_0'+str(hh)+'.png'
		subtexto='[Day 284 of 2009, 0'+str(hh)+'h]'
	else:
		entrada='./entrada/mtec02_284_'+str(hh)+'.dat'
		saida='./saida/mtec02_284_'+str(hh)+'.png'
		subtexto='[Day 284 of 2009, '+str(hh)+'h]'
	
	arq=open(entrada,'r')
	dados=arq.readlines()
	arq.close()
	
	x=[]
	y=[]
	z=[]
	matriz=[]
	
	for i in range(0,len(dados)):
		x.append(float(dados[i][1:7]))
		y.append(float(dados[i][8:14]))
		z.append(float(dados[i][15:21]))
	
	#n=int(np.sqrt(len(dados)-1))
	for ln in range(0,65):
		matriz.append([])
		for col in range(0,54):
			matriz[ln].append(None)
	
	c=0
	for j in range(0,54):
		for i in range(0,65):
			matriz[i][j]=z[c]
			#matrizb[n-1-j][i]=z[c]
#			matrizb[j][i]=z[c]
			c=c+1
	
	vx=np.arange(x_min,x_max+0.001,1.0)
	vy=np.arange(y_min,y_max+0.001,1.0)
	vz=np.arange(0.0,120.001,15.0)
	tvz=tuple(vz)
	vz2=np.arange(0.0,120.001,15.0)
	
	fig=plt.figure(num=1,figsize=(paper_width/25.4,paper_height/25.4))
	sub1=plt.subplot(1,1,1)
	#plt.contourf(vx,vy,matriz,vz,color=cm.jet,interpolation="bilinear")
	#ctf=plt.contourf(matriz,vz,extent=(x_min,x_max,y_min,y_max),color=cm.jet)
	#plt.subplots_adjust(left=0.1,bottom=0.1,right=0.9,top=0.9,wspace=0.0,hspace=0.0)
	plt.subplots_adjust(left=0.0,bottom=0.0,right=1.0,top=1.0,wspace=0.0,hspace=0.0)
	im=plt.imshow(matriz,extent=(x_min,x_max,y_min,y_max),cmap=cm.jet,interpolation="bilinear",aspect='auto',vmin=0.0,vmax=120.0)
	mp=plt.imshow(image2,extent=(x_min,x_max,y_min,y_max),interpolation="bilinear",aspect='auto')
	#plt.colorbar(orientation="horizontal",ticks=vz2,fraction=0.05,drawedges=False,pad=0.10,shrink=1.0)
	eq=plt.plot(x_dipeq,y_dipeq)
	plt.setp(eq,color='#666666',linewidth=4.5)
	ct=plt.contour(vx,vy,matriz,vz,colors="w",linewidths=3.0)
	clabs=plt.clabel(ct,inline=1,fontsize=10,fmt="%d")
	plt.setp(clabs,weight="bold")
	#plt.colorbar(im,orientation="vertical",ticks=tvz,fraction=0.05)
	#pts=plt.plot(x,y,'k.')
	plt.axis([x_min,x_max,y_min,y_max])
	xmajors=MultipleLocator(x_major_step)
	xminors=MultipleLocator(x_minor_step)
	ymajors=MultipleLocator(y_major_step)
	yminors=MultipleLocator(y_minor_step)
	sub1.xaxis.set_major_locator(xmajors)
	sub1.xaxis.set_minor_locator(xminors)
	sub1.yaxis.set_major_locator(ymajors)
	sub1.yaxis.set_minor_locator(yminors)
	#sub1.xaxis.set_visible(False)
	#sub1.xaxis.set_visible(False)
	sub1.set_xticklabels([])
	sub1.set_yticklabels([])
	#titulo=plt.suptitle(u"Total Electron Content [electrons / m²] x 10E+16")
	#plt.setp(titulo,family="sans-serif",size=16,weight="bold",linespacing=2.0)
	#subtitulo=plt.title(subtexto)
	#plt.setp(subtitulo,family="sans-serif",size=16,weight="semibold",linespacing=2.0)
	#rotulox=plt.xlabel(u"\nGeographic Longitude [degrees]")
	#plt.setp(rotulox,family="sans-serif",size=14,weight="semibold")
	#rotuloy=plt.ylabel(u"Geographic Latitude [degrees]")
	#plt.setp(rotuloy,family="sans-serif",size=14,weight="semibold")
	plt.savefig(saida)
	plt.close(1)
