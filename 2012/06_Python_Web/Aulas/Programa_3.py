import urllib2
from BeautifulSoup import BeautifulSoup

url = "http://www.google.com.br"

request = urllib2.Request(url)
response = urllib2.urlopen(request)
document = response.read()

#normaliza o documento para que o mesmo seja acessivel via objetos
soup = BeautifulSoup(document) 

# retorna uma lista com todos os links do documento
links = soup.findAll('a')  

for link in links:
    print link['href']
	
# href = comando que colocamos no html para linkar
	
#obs: neste caso teremos apenas os links , nao o texto escrito em html 

#Como voce pode ver, o BeautifulSoup e quase uma mae quando o assunto e extrair informacoes de HTML , pois hoje em dia
# as pessoas escrevem os codigos muito errado