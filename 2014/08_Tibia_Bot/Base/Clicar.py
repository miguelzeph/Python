import time
import win32api, win32con

#Clicar
def leftClick():
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	time.sleep(.001)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
	
#Pegar Coordena
def get_cords():
	x,y = win32api.GetCursorPos()
	print "Coordenada X: ",x,", Coordenada Y: ",y
	coordenada = [x,y]
	return coordenada

#Posicao do Mouse
def mousePos(cord):
    win32api.SetCursorPos((cord[0],cord[1]))



#Programa Principal
def programa():
	time.sleep(4)
	coordenada = get_cords()
	mousePos([142,540])
	for tempo in range(0,1000):
		leftClick()
			
			



	