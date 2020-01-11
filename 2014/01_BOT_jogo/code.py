#google Cromer 90% resolution
import ImageGrab
import os
import time
import win32api, win32con
import ImageOps
from numpy import *


x_pad,y_pad = 247,295
	
def get_cords_ref():
        global x_pad,y_pad #essa func, faz trocar a variavel quando vc chama o def ()
        x_pad,y_pad = win32api.GetCursorPos()
        print x_pad,y_pad
	

def screenGrab():
	box= (x_pad +1,y_pad +1,x_pad +574,y_pad +431)
	im = ImageGrab.grab(box)
	#im.save(os.getcwd()+'\\full_snap__'+str(int(time.time()))+'.png','PNG')
	return im

def grab():
    box = (x_pad + 1,y_pad+1,x_pad+574,y_pad+431)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    return a

def leftClick():
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	time.sleep(.1) #Ele faz isso para o programa deixar o jogo atualizar algo
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
	print "Click."
	
def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    print 'left Down'
         
def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)
    print 'left release'

def mousePos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))

def get_cords(): #serve para ajudar a pegar a coordenada
    x,y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print x,',',y

def startGame():
    #location of first menu
    mousePos((287, 194))
    leftClick()
    time.sleep(.1)
     
    #location of second menu
    mousePos((242,349))
    leftClick()
    time.sleep(.1)
     
    #location of third menu
    mousePos((519,411))
    leftClick()
    time.sleep(.1)
     
    #location of fourth menu
    mousePos((269,335))
    leftClick()
    time.sleep(.1)


class Cord:
     
    f_shrimp = (41 , 305)
    f_rice = (88 , 307)
    f_nori = (35 , 353)
    f_roe = (86 , 352)
    f_salmon = (34 , 404)
    f_unagi = (80 , 404)

    phone = (522,319)

    menu_toppings = (481,248)

    t_shrimp =(437,200)
    t_unagi =(513,200)
    t_nori =(437,253)
    t_roe =(515,245)
    t_salmon =(444,297)
    t_exit =(536,302)

    menu_rice = (479 , 266)
    buy_rice = (485 , 256)
     
    delivery_norm = (439 , 265)

# Posicao dos Pratos

#82,188
#177,188
#266,188
#356,188
#448,188
#542,188

def clear_tables():
     
    mousePos((82,188))
    leftClick()
 
    mousePos((177,188))
    leftClick()
 
    mousePos((266,188))
    leftClick()
 
    mousePos((356,188))
    leftClick()
 
    mousePos((448,188))
    leftClick()
 
    mousePos((538,188))
    leftClick()
    time.sleep(1)

# Receitas:

# Caliroll = 1 rice, 1 nori, 1 roe
# Onigiri = 2 rices, 1 nori
# Gunkan = 1 rice, 1 nori, 2 roe


def foldMat():
    mousePos((Cord.f_rice[0]+40,Cord.f_rice[1])) #clica na tabua
    leftClick()
    time.sleep(.1)

foodOnHand = {'shrimp':5,
              'rice':10,
              'nori':10,
              'roe':10,
              'salmon':5,
              'unagi':5}


def makeFood(food):
    if food == 'caliroll':
        print 'Making a caliroll'
        foodOnHand['rice'] -= 1
        foodOnHand['nori'] -= 1
        foodOnHand['roe'] -= 1 
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.1)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.1)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(1.5)
     
    elif food == 'onigiri':
        print 'Making a onigiri'
        foodOnHand['rice'] -= 2
        foodOnHand['nori'] -= 1
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.1)
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.1)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(1.5)
 
    elif food == 'gunkan':
        print 'Making a gunkan'
        foodOnHand['rice'] -= 1 
        foodOnHand['nori'] -= 1 
        foodOnHand['roe'] -= 2 
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.1)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.1)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.1)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(1.5)

        



#Saber a cor de um ponto qualquer do mouse ----------------
    
def teste_color(): 
    x_teste,y_teste = win32api.GetCursorPos() #posicao
    x_teste = x_teste - x_pad #posicao x e arrumando ref
    y_teste = y_teste - y_pad #posicao y e arrumando ref
    teste = x_teste,y_teste
    cor = screenGrab() #Screen Shoot

    
    #print cor.getpixel(teste)
    print cor.getpixel(Cord.buy_rice)
    print cor.getpixel(Cord.t_nori)
    print cor.getpixel(Cord.t_roe)
    

    
#----------------------------------------------------------
    

def buyFood(food):
     
    if food == 'rice':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_rice)
        time.sleep(.05)
        leftClick()
        s = screenGrab()
        if s.getpixel(Cord.buy_rice) != (255, 250, 208):
            print 'rice is available'
            mousePos(Cord.buy_rice)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['rice'] += 10     
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print 'rice is NOT available'
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)
             
 
             
    if food == 'nori':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_toppings)
        time.sleep(.05)
        leftClick()
        s = screenGrab()
        print 'test'
        time.sleep(.1)
        if s.getpixel(Cord.t_nori) != (33, 30, 11):
            print 'nori is available'
            mousePos(Cord.t_nori)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['nori'] += 10
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print 'nori is NOT available'
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)
 
    if food == 'roe':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_toppings)
        time.sleep(.05)
        leftClick()
        s = screenGrab()
         
        time.sleep(.1)
        if s.getpixel(Cord.t_roe) != (101, 13, 13):
            print 'roe is available'
            mousePos(Cord.t_roe)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['roe'] += 10
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print 'roe is NOT available'
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)


def checkFood():
    for i, j in foodOnHand.items():
        if i == 'nori' or i == 'rice' or i == 'roe':
            if j <= 4:
                print '%s is low and needs to be replenished' % i
                buyFood(i)


def get_seat_one():
    box = (270,350,325,362)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    #print a
    #im.save(os.getcwd() + '\\seat_one__' + str(int(time.time())) + '.png', 'PNG')    
    return a
 
def get_seat_two():
    box = (361,350,416,362)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    #print a
    #im.save(os.getcwd() + '\\seat_two__' + str(int(time.time())) + '.png', 'PNG')    
    return a
 
def get_seat_three():
    box = (452,350,507,362)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    #print a
    #im.save(os.getcwd() + '\\seat_three__' + str(int(time.time())) + '.png', 'PNG')    
    return a
 
def get_seat_four():
    box = (543,350,598,362)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    #print a
    #im.save(os.getcwd() + '\\seat_four__' + str(int(time.time())) + '.png', 'PNG')    
    return a
 
def get_seat_five():
    box = (634,350,689,362)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    #print a
    #im.save(os.getcwd() + '\\seat_five__' + str(int(time.time())) + '.png', 'PNG')    
    return a
 
def get_seat_six():
    box = (725,350,780,362)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    #print a
    #im.save(os.getcwd() + '\\seat_six__' + str(int(time.time())) + '.png', 'PNG')    
    return a
 
def get_all_seats():
    get_seat_one()
    get_seat_two()
    get_seat_three()
    get_seat_four()
    get_seat_five()
    get_seat_six()

#mesa 1,2,5,6
sushiTypes_1 = {1750:'onigiri',
             2267:'caliroll',
             1630:'gunkan',}
#mesa 3,4
sushiTypes_2 = {1623:'onigiri',
             2331:'caliroll',
             1694:'gunkan',}


#sem cliente
class Blank:
    seat_1 = 6065
    seat_2 = 4467
    seat_3 = 9564
    seat_4 = 9570
    seat_5 = 5800
    seat_6 = 8106


#The basic flow will follow this: Check seats > if customer,
#make order > check food > if low, buy food > clear tables >
#repeat.

def check_bubs():
 
    checkFood()
    s1 = get_seat_one()
    if s1 != Blank.seat_1:
        #interessante essa funcao has_key()
        #interessante e que ele nao precisa criar outros if e else para saber
        #Qual dos tres tipos de comida ele quer... apenas o tipo s1
        if sushiTypes_1.has_key(s1):
            print 'table 1 is occupied and needs %s' % sushiTypes_1[s1]
            makeFood(sushiTypes_1[s1])
        else:
            print 'sushi not found!\n sushiType = %i' % s1
 
    else:
        print 'Table 1 unoccupied'
 
    clear_tables()
    checkFood()
    s2 = get_seat_two()
    if s2 != Blank.seat_2:
        if sushiTypes_1.has_key(s2):
            print 'table 2 is occupied and needs %s' % sushiTypes_1[s2]
            makeFood(sushiTypes_1[s2])
        else:
            print 'sushi not found!\n sushiType = %i' % s2
 
    else:
        print 'Table 2 unoccupied'
 
    checkFood()
    s3 = get_seat_three()
    if s3 != Blank.seat_3:
        if sushiTypes_2.has_key(s3):
            print 'table 3 is occupied and needs %s' % sushiTypes_2[s3]
            makeFood(sushiTypes_2[s3])
        else:
            print 'sushi not found!\n sushiType = %i' % s3
 
    else:
        print 'Table 3 unoccupied'
 
    checkFood()
    s4 = get_seat_four()
    if s4 != Blank.seat_4:
        if sushiTypes_2.has_key(s4):
            print 'table 4 is occupied and needs %s' % sushiTypes_2[s4]
            makeFood(sushiTypes_2[s4])
        else:
            print 'sushi not found!\n sushiType = %i' % s4
 
    else:
        print 'Table 4 unoccupied'
 
    clear_tables()
    checkFood()
    s5 = get_seat_five()
    if s5 != Blank.seat_5:
        if sushiTypes_1.has_key(s5):
            print 'table 5 is occupied and needs %s' % sushiTypes_1[s5]
            makeFood(sushiTypes_1[s5])
        else:
            print 'sushi not found!\n sushiType = %i' % s5
 
    else:
        print 'Table 5 unoccupied'
 
    checkFood()
    s6 = get_seat_six()
    if s6 != Blank.seat_6:
        if sushiTypes_1.has_key(s6):
            print 'table 1 is occupied and needs %s' % sushiTypes_1[s6]
            makeFood(sushiTypes_1[s6])
        else:
            print 'sushi not found!\n sushiType = %i' % s6
 
    else:
        print 'Table 6 unoccupied'
 
    clear_tables()


def main():
        startGame()
        
        while True:
                check_bubs()












        
	
    
