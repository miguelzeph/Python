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

#Digite a Url que contem os Link
url = 'http://www.las.inpe.br/~mev/usuarios-mev/'

request = urllib2.Request(url)
response = urllib2.urlopen(request)
document = response.read()

#normaliza o documento para que o mesmo seja acessivel via objetos
soup = BeautifulSoup(document) 

# retorna uma lista com todos os links do documento
links = soup.findAll('a')  
#print links
#raw_input()

for pasta in links:
	
	print pasta['href']
	Filtro = raw_input("Escolha : S ou N ")
	
	if Filtro == 's':
		url_novo = 'http://www.las.inpe.br/~mev/usuarios-mev/'+pasta['href']
		
		request_novo = urllib2.Request(url_novo)
		response_novo = urllib2.urlopen(request_novo)
		document_novo = response_novo.read()
		soup_novo = BeautifulSoup(document_novo) 
		links_novo = soup_novo.findAll('a')  
		
		for pdf in links_novo:
			
			arquivo= pdf['href']
			
			#--------
			#print arquivo
			#raw_input()
			#--------
			if (jpg(arquivo) == '.jpg' or jpg(arquivo) == '.tif'):
			
				download = url_novo+arquivo
				#------
				#print download
				#raw_input()
				#------
				
				urllib.urlretrieve(download,arquivo)
				print 'download'
				
			else:
				continue	