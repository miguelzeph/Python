#!/usr/bin/env python
#! -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np

arq=open("./error_ccir_cp_edt.txt","r")
dados=arq.readlines()
arq.close()

x=[]
y=[]

for i in range(0,len(dados)):
	x.append(float(dados[i][0:15]))
	y.append(float(dados[i][57:63]))

paper_width=300.0
paper_height=300.0
axes_linewidth=2
axes_label_paddding=10.0
axes_label_fontsize=12
major_ticks_size=15
minor_ticks_size=8
x_min=1990.0
x_max=2012.0
x_major_step=5.0
x_minor_step=1.0
y_min=-0.5
y_max=1.0
y_major_step=0.2
y_minor_step=0.05
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
plt.rcParams["savefig.dpi"]=300
fig=plt.figure(num=1,figsize=(paper_width/25.4,paper_height/25.4))
sub1=plt.subplot(1,1,1)
pts=plt.plot(x,y,'k.')
plt.setp(pts,markersize=1.0,markeredgewidth=0.0)
line0=plt.plot([x_min,x_max],[0.0,0.0],'r-')
plt.setp(line0,linewidth=1.5)
plt.axis([x_min,x_max,y_min,y_max])
xmajors=MultipleLocator(x_major_step)
xminors=MultipleLocator(x_minor_step)
ymajors=MultipleLocator(y_major_step)
yminors=MultipleLocator(y_minor_step)
sub1.xaxis.set_major_locator(xmajors)
sub1.xaxis.set_minor_locator(xminors)
sub1.yaxis.set_major_locator(ymajors)
sub1.yaxis.set_minor_locator(yminors)
titulo=plt.suptitle("Cachoeira Pta., EDITED data, CCIR, (IRI - Ionosonde) / Ionosonde, foF2")
plt.setp(titulo,family="sans-serif",size=16,weight="bold",linespacing=2.0)
rotulox=plt.xlabel("\nYear")
plt.setp(rotulox,family="sans-serif",size=14,weight="semibold")
rotuloy=plt.ylabel("(foF2_IRI - foF2_IONO) / foF2_IONO\n")
plt.setp(rotuloy,family="sans-serif",size=14,weight="semibold")
plt.grid(True)
plt.savefig("./error_ccir_cp_edt.png")#ou poderia mostrar direto 
#plt.show()
