#DICA PRINCIPAL.... APERTE F12 NO CROME E VEJA O CODIGO PARA SABER O QUE ESTA FAZENDO... (CONSOLE JAVA)
# coding: UTF-8

import urllib2
from BeautifulSoup import BeautifulSoup
import urllib


url = "http://eupodiatamatando.com/downloads/cursos.html"

request = urllib2.Request(url)
response = urllib2.urlopen(request)
soup = BeautifulSoup(response.read()) 

links = soup.findAll('a')# procura todos os <a>...</a>

for linha in links:
   
   #print  linha['href'] #vai me dar os links ... pois os links estao no href = ....
   print  linha.string # aqui eu quero apenas a string dentro do <>....<>
   
   

#cd_programa e do codigo html ... se quizer ver crie este programa veja...-----------

#url = "http://eupodiatamatando.com/downloads/cursos.html"

#request = urllib2.Request(url)
#response = urllib2.urlopen(request)

#tree=BeautifulSoup(response.read())

#print tree

#-----------------------