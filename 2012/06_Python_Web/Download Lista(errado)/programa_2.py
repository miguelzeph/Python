
import urllib2
import re
from BeautifulSoup import BeautifulSoup

page = urllib2.urlopen("http://animemundobr.blogspot.com/2007/11/samurai-x-dublado.html")
soup = BeautifulSoup(page)
links = soup.findAll("a",href=re.compile("http://rapidshare.com/"))
lista = []
for link in links:
	lista.append(link) 
print lista

raw_input()
f = open("samurai_x_links.txt","w")
f.write('\n'.join(lista))
f.close()