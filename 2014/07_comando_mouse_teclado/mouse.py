import win32api,win32con
import time
#------------MOUSE--------------
def leftClick():
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	time.sleep(.01)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
	
def get_cords(variavel):
	x,y = win32api.GetCursorPos()
	coordenada = [x,y+variavel]
	return coordenada

def mousePos(cord):
    win32api.SetCursorPos((cord[0],cord[1]))
	

mousePos(get_cords(9))
time.sleep(1)
leftClick()