#funciona para 2.7
from urllib import *

#Vai abaixar uma imagem 
urlretrieve('https://www.google.com.br/search?q=bola&es_sm=93&source=lnms&tbm=isch&sa=X&ei=27-2U8nXM6bIsATL9oGQDg&ved=0CAYQ_AUoAQ&biw=741&bih=683&dpr=0.9#facrc=_&imgdii=_&imgrc=EGxJPuMZdpnN0M%253A%3BhBmyq0Fqg5f1TM%3Bhttp%253A%252F%252Fgloboesporte.globo.com%252Fplatb%252Ffiles%252F169%252F2012%252F07%252Fbola.jpg%3Bhttp%253A%252F%252Fgloboesporte.globo.com%252Fpe%252Ftorcedor-nautico%252Fplatb%252F2012%252F07%252F30%252Fnao-e-a-bola-que-deve-ser-marcada%252F%3B300%3B300', 'bola.png')

#Apaga os Caches
urlcleanup()
