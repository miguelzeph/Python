import Blender
import math
import time

scn=Blender.Scene.GetCurrent()

c=1
d=1
e=1
#SELECIONE O OBJETO
for i in range(60):
	Blender.Object.Duplicate()
	objAct=scn.getActiveObject()
	
	objAct.setLocation(d,math.tan(e),math.tan(c))
	
	c+=1
	d+=1
	e+=3
	#Da uma pausa de 0.2 seg..
	time.sleep(0.2)
	
	Blender.Redraw()