import urllib
import urllib2
from BeautifulSoup import BeautifulSoup

def jpg(nome):

	N = len(nome)
	
	return nome[N-4::]

#----------Diretorio-------------
import os 
#diretorio_principal=os.getcwd()
os.chdir('./Arquivos')
#--------------------------------

#Digite a Url que contem os Links
url = 'http://www.las.inpe.br/~mev/usuarios-mev/Miguel-Baldan/29-07-2013/'

request = urllib2.Request(url)
response = urllib2.urlopen(request)
document = response.read()

#normaliza o documento para que o mesmo seja acessivel via objetos
soup = BeautifulSoup(document) 

# retorna uma lista com todos os links do documento
links = soup.findAll('a')  

for pdf in links:
	
	arquivo= pdf['href']
	#Dica: aperte F12 no site desejavel e entao entendera os comandos
	
	
	if jpg(arquivo) == '.jpg':
	
		
		download = url+'/'+arquivo
		urllib.urlretrieve(download,arquivo)
		print 'download'
	
	else:
		continue
	