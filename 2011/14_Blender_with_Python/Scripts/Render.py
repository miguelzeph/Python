import Blender
from Blender import *
from Blender.Scene import Render
 
scn = Scene.GetCurrent()
context = scn.getRenderingContext()
 
Render.EnableDispWin()
context.extensions = True
context.renderPath = "//myRenderdir/"
context.sizePreset(Render.PC)
context.imageType = Render.AVIRAW
context.sFrame = 2
context.eFrame = 10
context.renderAnim()
 
context.imageType = Render.TARGA
context.fps = 15
context.sFrame = 15
context.eFrame = 22
context.renderAnim()
 
Render.CloseRenderWindow()
print context.fps
print context.cFrame