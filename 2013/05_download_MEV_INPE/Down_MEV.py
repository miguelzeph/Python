import urllib
import urllib2
from BeautifulSoup import BeautifulSoup

#----------Diretorio-------------
import os 
#diretorio_principal=os.getcwd()
os.chdir('./Arquivos')
#--------------------------------

#Digite a Url que contem os Links
url = 'http://www.las.inpe.br/~mev/usuarios-mev/Belchior'

request = urllib2.Request(url)
response = urllib2.urlopen(request)
document = response.read()

#normaliza o documento para que o mesmo seja acessivel via objetos
soup = BeautifulSoup(document) 

# retorna uma lista com todos os links do documento
links = soup.findAll('a')  

for pdf in links:
	
	arquivo= pdf['href']
	 
	print 'Nome do Arquivo : '+arquivo
	
	condicao = raw_input('\nDeseja Salvar "s" ou "n" ?\n')
	print "-------------------------------------"
	
	if condicao == 's':
	
		
		download = url+'/'+arquivo
		urllib.urlretrieve(download,arquivo)
	
	else:
		continue
	