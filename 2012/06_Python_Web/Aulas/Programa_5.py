from BeautifulSoup import BeautifulSoup
import urllib
import urllib2

base_url = 'http://sourceforge.net'
busca = raw_input('Pesquisar por: ')

variaveis_get = urllib.urlencode({'type_of_search':'soft','words':busca})
req = urllib2.Request(base_url+'/search/',variaveis_get)
response = urllib2.urlopen(req).read()

soup = BeautifulSoup(response)
# procura pela tabela com id=searchtable
tabela = soup.find('table',{'id':'searchtable'}) 
#retorna uma lista com todas as linhas (&lt;tr&gt;) da tabela
linhas_tabela = tabela.findAll('tr') 

i=0

for linha in linhas_tabela:
    i+=1
    #encontra a primeira coluna (descricao) da linha
    coluna_descricao = linha.find('td') 

    #o atributo contents contem uma lista com o conteudo da tag
    nome_projeto = coluna_descricao.find('a').contents[0] 

    descricao_projeto = coluna_descricao.contents[2].strip()
    print 'Projeto '+str(i)+': '+nome_projeto
    print descricao_projeto
    print '--------------------------------'