import urllib2
from BeautifulSoup import BeautifulSoup

url = "http://www.google.com.br"

request = urllib2.Request(url)
response = urllib2.urlopen(request)
document = response.read()

#normaliza o documento para que o mesmo seja acessivel via objetos
soup = BeautifulSoup(document) 

# retorna uma lista com todos os links do documento
links = soup.findAll('a') # este a e porque em html quando queremos colocar link entra <a ref.... 

for link in links:
    print link