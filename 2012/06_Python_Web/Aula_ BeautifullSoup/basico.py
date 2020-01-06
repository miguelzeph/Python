from BeautifulSoup import BeautifulSoup

#arq=file('C:\Users\Miguel\Desktop\python web\Aula_ BeautifullSoup\Teste.html')
arq=file('./Teste.html')
tree=BeautifulSoup(arq.read())

print tree('title'),'\n'

print tree('title')[0],'\n'

print tree('title')[0].string,'\n'

print len(tree('table')[0]('td')),'\n'

#explicacao:

#tree(nome)[numero do nome (como so temos 1 table coloca-se 0)] , mas no caso do "td" temos varios outros por isto o loop
# .string = e para escrever

print tree('table')[0]('td')[0].string,'\n'

v=len(tree('table')[0]('td'))

print '\n---INICIO DO LOOP---\n'

for i in range(v):
	print tree('table')[0]('td')[i].string,'\n'