from BeautifulSoup import BeautifulSoup
import urllib,urllib2
from subprocess import call

base_url = 'http://sourceforge.net'
busca = raw_input('Pesquisar por: ')

variaveis_get = urllib.urlencode({'type_of_search':'soft','words':busca})
req = urllib2.Request(base_url+'/search/',variaveis_get)
response = urllib2.urlopen(req).read()

soup = BeautifulSoup(response)

# procura pela tabela com id=searchtable
tabela = soup.find('table',{'id':'searchtable'}) 

 #retorna uma lista com todas as linhas da tabela
linhas_tabela = tabela.findAll('tr')

i=0
links_download = []

for linha in linhas_tabela:
    i+=1
    coluna_descricao = linha.find('td')
    nome_projeto = coluna_descricao.find('a').contents[0]
    link_download = linha.find('a',{'class':'downloadnow'})['href']
    links_download.append(link_download)
    descricao_projeto = coluna_descricao.contents[2].strip()
    print 'Projeto '+str(i)+': '+nome_projeto
    print descricao_projeto
    print '--------------------------------'

opcao = int(raw_input('Qual projeto gostaria de baixar? '))
opcao_url = base_url+links_download[opcao-1]
call(['wget',opcao_url]) #chama o wget com o link para download