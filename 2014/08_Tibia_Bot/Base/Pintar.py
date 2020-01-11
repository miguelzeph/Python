import win32api,win32con
import time


#Pegar Coordenada
def get_cords():
	x,y = win32api.GetCursorPos()
	print "Coordenada X: ",x,"Coordenada Y: ", y	
#Clicar
def leftclick():
	#Segura
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	time.sleep(.01)
	#Solta
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
	#print ('left click')

#Posicao do Mouse
def mousePos(cord):
	win32api.SetCursorPos((cord[0],cord[1]))
	
#Programa Principal
def Pintar():
	cord = [input('X:'), input('Y:')]
	time.sleep(5)
	mousePos(cord)
	
	for x in range(cord[0],cord[0]+30):
		for y in range(cord[1],cord[1]+30):
			mousePos([x,y])
			leftclick()
	print 'Pintou'