import win32api,win32con
import time
import ImageGrab
import os
import ImageOps
import numpy

#Pegar Coordenada (PRINT)
def get_cords():
	x,y = win32api.GetCursorPos()
	print "Coordenada X: ",x,"Coordenada Y: ", y
	
#Pegar Coordenada (DIRETO)
def cords():
	x,y = win32api.GetCursorPos()
	cordenadas=[x,y]
	return cordenadas

#Caso vc queira trabalhar com uma func Referencial	
x_pad,y_pad = 247,295	
def get_cords_ref():
        global x_pad,y_pad #Atualiza a variavel x_pad,ypad quando vc chama o def ()
        x_pad,y_pad = win32api.GetCursorPos()
        print x_pad,y_pad

#Clicar
def leftclick():
	#Segura
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	time.sleep(.1)
	#Solta
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
	print ('left click')

#Posicao do Mouse
def mousePos(cord):
	win32api.SetCursorPos((cord[0],cord[1]))
	
#Foto - Screen Shoot
def Foto(cord):
	box =(cord[0],cord[1],cord[0]+2,cord[1]+2)
	im = ImageGrab.grab(box)
	return im
	
#Foto - Screen Shoot - Salvando
def Foto_salvar1(cord1,cord2):
	box =(cord1[0],cord1[1],cord2[0],cord2[1]) #Pegar uma "caixa"
	im = ImageGrab.grab(box)
	im.save(os.getcwd()+'\\full_snap__'+str(int(time.time()))+'.png','PNG')
	return im
def Foto_salvar2(): # Mais aprimorada
	raw_input("Pegue a coordenada 1")
	cord1 = cords()
	raw_input("Pegue a coordenada 2")
	cord2 = cords()
	box =(cord1[0],cord1[1],cord2[0],cord2[1]) #Pegar uma "caixa"
	im = ImageGrab.grab(box)
	im.save(os.getcwd()+'\\full_snap__'+str(int(time.time()))+'.png','PNG')
	return im
	
#Reconhecer Cor
def teste_cor(cord):
	cor = Foto(cord)
	#print cor.getpixel((cord[0],cord[1]))
	return cor.getpixel((1,1))

#Teste Cor Rapido
def rapido_cor():
	cor = Foto(cords())
	print cor.getpixel((1,1))

#Testa a somatoria de corres ( quantidade de branco e preto )	
#def grab(cor1,cord2):
def grab(cord1,cord2):
	box = (cord1[0],cord1[1],cord2[0],cord2[1])
	im = ImageOps.grayscale(ImageGrab.grab(box))
	vetor = numpy.array(im.getcolors())
	vetor = vetor.sum()
	#print vetor
	return vetor



	




