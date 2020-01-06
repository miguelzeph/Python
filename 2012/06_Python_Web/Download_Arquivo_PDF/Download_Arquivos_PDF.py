import urllib
import urllib2
from BeautifulSoup import BeautifulSoup

#----------Diretorio
import os 
#diretorio_principal=os.getcwd()
os.chdir('./Arquivos')
#----------

url = 'http://www.fing.edu.uy/if/cursos/fismod/cederj'

request = urllib2.Request(url)
response = urllib2.urlopen(request)
document = response.read()

#normaliza o documento para que o mesmo seja acessivel via objetos
soup = BeautifulSoup(document) 

# retorna uma lista com todos os links do documento
links = soup.findAll('a')  

for pdf in links:
	nome= pdf['href']
	
	arquivo = url+'/'+nome
	
	
	
	urllib.urlretrieve(arquivo,nome)
	
	
# href = comando que colocamos no html para linkar	
