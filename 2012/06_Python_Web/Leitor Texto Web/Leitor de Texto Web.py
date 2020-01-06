#coding: utf-8
#fonte : http://eupodiatamatando.com/tag/python/
import urllib


pagina = urllib.urlopen("http://eupodiatamatando.com/downloads/cursos.html")
for linha in pagina:
   if linha.find("cd_programa") != -1:#find e uma func do python
      tmp = linha.split('>', 1)[1]#ou seja ... <>...utilizando a biblioteca BeuatifullSoup nao precisamos
      nome = tmp.split('< ', 1)[0]
      print nome
pagina.close()

#cd_programa e do codigo html ... se quizer ver crie este programa veja...-----------

#url = "http://eupodiatamatando.com/downloads/cursos.html"

#request = urllib2.Request(url)
#response = urllib2.urlopen(request)

#tree=BeautifulSoup(response.read())

#print tree

#-----------------------