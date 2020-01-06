import urllib as url

f = url.urlopen('http://www.google.com.br')

#copie este f.read() em um doc html e vera a pagina
print f.read()