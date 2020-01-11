import win32com.client
import time

#Visualizar Monstro-------------------------------------
import win32api,win32con
import ImageOps
import ImageGrab
import numpy

def grab(cord1,cord2):
	
	box = (cord1[0],cord1[1],cord2[0],cord2[1])
	im = ImageOps.grayscale(ImageGrab.grab(box))
	vetor = numpy.array(im.getcolors())
	vetor = vetor.sum()
	#print vetor
	return vetor
	
def leftClick():
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	time.sleep(.01)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
	
def get_cords():
	x,y = win32api.GetCursorPos()
	print "Coordenada X: ",x,", Coordenada Y: ",y
	coordenada = [x,y]
	return coordenada

def mousePos(cord):
    win32api.SetCursorPos((cord[0],cord[1]))
#-------------------------------------------------------




#-------------TECLADO-----------
wsh = win32com.client.Dispatch("WScript.Shell")
def esquerda():
	wsh.SendKeys("{LEFT}")
def direita():
	wsh.SendKeys("{RIGHT}")
def baixo():
	wsh.SendKeys("{DOWN}")
def cima():
	wsh.SendKeys("{UP}")

#AQUI ELE VE SE TEM INIMIGO, Se nao , Ele anda	
def esq(numero):
	for i in range(0,numero):
		time.sleep(1.5)
		if  grab([434, 260],[440, 264]) != 784:
			esquerda()
			time.sleep(0.8)
		else:
			time.sleep(7)
			if grab([434, 260],[440, 264]) != 784:
				esquerda()
			else:
				time.sleep(7)
		
def dir(numero):
	for i in range(0,numero):
		time.sleep(1.5)
		if  grab([434, 260],[440, 264]) != 784:
			direita()
			time.sleep(0.8)
		else:
			time.sleep(7)
			if grab([434, 260],[440, 264]) != 784:
				direita()
			else:
				time.sleep(7)
		
def cim(numero):
	for i in range(0,numero):
		time.sleep(1.5)
		if  grab([434, 260],[440, 264]) != 784:
			cima()
			time.sleep(0.8)
		else:
			time.sleep(7)
			if grab([434, 260],[440, 264]) != 784:
				cima()
			else:
				time.sleep(7)
		
def bai(numero):
	for i in range(0,numero):
		time.sleep(1.5)
		if  grab([434, 260],[440, 264]) != 784:
			baixo()
			time.sleep(0.8)
		else:
			time.sleep(7)
			if grab([434, 260],[440, 264]) != 784:
				baixo()
			else:
				time.sleep(7)
#------------------------------------------------------			


#Caminho Asmord
def caminho_Asmord():
	
	#Ida --->
	bai(4);dir(9);bai(4);dir(10);bai(7);dir(2);bai(1);dir(14)
	#Volta <----
	esq(14);cim(1);esq(2);cim(7);esq(10);cim(4);esq(9);cim(4)
	
	

#PROGRAMA PRINCIPAL	
def programa():	
	
	for i in range(0,10):
		time.sleep(0.8)
		caminho_Asmord()
		
	
programa()

print ('acabou andar')