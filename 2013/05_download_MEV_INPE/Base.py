#Somente para ver os prints e os erros...

import urllib
import urllib2
from BeautifulSoup import BeautifulSoup

#----------Diretorio
import os 
#diretorio_principal=os.getcwd()
os.chdir('./Arquivos')
#----------

url = 'http://www.las.inpe.br/~mev/usuarios-mev/Lilian/'

request = urllib2.Request(url)
response = urllib2.urlopen(request)
document = response.read()

#normaliza o documento para que o mesmo seja acessivel via objetos
soup = BeautifulSoup(document) 

# retorna uma lista com todos os links do documento
links = soup.findAll('a')  

for pdf in links:
	
	arquivo= pdf['href']
	
	#if arquivo=='programa.pdf':
	#	continue
	#else: 
	print arquivo
	#print url
	#print pdf
		
	download = url+'/'+arquivo
		
	#raw_input()
	#urllib.urlretrieve(download,arquivo)
	
	
# href = comando que colocamos no html para linkar	
