import win32com.client
import win32api,win32con
import time
import ImageGrab
import os
import ImageOps
import numpy
import random

#-------------TECLADO-----------
wsh = win32com.client.Dispatch("WScript.Shell")
def esquerda(n):
	wsh.SendKeys("{LEFT}"*n)
def direita(n):
	wsh.SendKeys("{RIGHT}"*n)
def baixo(n):
	wsh.SendKeys("{DOWN}"*n)
def cima(n):
	wsh.SendKeys("{UP}"*n)
	
#------------MOUSE--------------
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
	
def Foto_salvar1(cord1,cord2):
	box =(cord1[0],cord1[1],cord2[0],cord2[1]) #Pegar uma "caixa"
	im = ImageGrab.grab(box)
	im.save(os.getcwd()+'\\full_snap__'+str(int(time.time()))+'.png','PNG')
	return im
	
def grab(cord1,cord2):
	
	box = (cord1[0],cord1[1],cord2[0],cord2[1])
	im = ImageOps.grayscale(ImageGrab.grab(box))
	vetor = numpy.array(im.getcolors())
	vetor = vetor.sum()
	#print vetor
	return vetor

#Sorteia qual direcao vai o personagem
def sorteio():
	v = [1,2,3,4]
	
	sorteio = random.choice
	
	if sorteio(v) == 1:
		esquerda(1)	
	if sorteio(v) == 2:
		direita(1)	
	if sorteio(v) == 3:
		baixo(1)	
	if sorteio(v) == 4:
		cima(1)
	
#--------PODERES DO JOGO ---------

def livro_vida():
	mousePos([601,332])
	time.sleep(1.2)
	leftClick()
	
def livro_ataque():
	mousePos([636,370])
	time.sleep(1.2)
	leftClick()

def skill_ata():
	mousePos([584, 451])
	time.sleep(1.2)
	leftClick()

def skill_def():
	mousePos([620, 448])
	time.sleep(1.2)
	leftClick()

#PROGRAMA PRINCIPAL	
def programa():	
	
	mousePos(get_cords())
	time.sleep(1.2)
	leftClick()
	
	for t in range(0,20):
		
		#TEMPO DE ATAQUE
		if t%9 == 0:
			#Tempo q dou para ele matar algo
			time.sleep(5)
		#ANDAR RANDOM
		#time.sleep(0.8)
		#sorteio()
		
		#SKILL
		
		#Skill Ataque
		if t%10 == 0:
			mousePos([585,453])
			time.sleep(1)
			leftClick()
		#Skill Defesa
		if t%6 == 0:
			mousePos([623,445])
			time.sleep(0.8)
			leftClick()
		
		
		#MAGIAS

		#VIDA BAIXA
		if  grab([132,235],[141,242]) != 1015 :#731

			#Mana minima para utilizar magia
			if grab([114,249],[117,256]) == 853:
			
				mousePos([601,332])
				time.sleep(0.8)
				leftClick()
				
			#Frasco	
			else:
				mousePos([560, 411])
				time.sleep(0.8)
				leftClick()



		#Magia Ataque
		#HP MAXIMO
		#if  grab([164,237],[166,239]) == 253:

			#MANA MAXIMO
		#	if grab([154,251],[157,256]) == 524:
			
		#		mousePos([636,370])
		#		time.sleep(0.8)
		#		leftClick()
		
		
		
		
		
		
		
		
		
		