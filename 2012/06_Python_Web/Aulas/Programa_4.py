import urllib
import urllib2

base_url = 'http://sourceforge.net'
busca = raw_input('Pesquisar por: ')

variaveis_get = urllib.urlencode({'type_of_search':'soft','words':busca})
req = urllib2.Request(base_url+'/search/',variaveis_get)
response = urllib2.urlopen(req).read()
print response