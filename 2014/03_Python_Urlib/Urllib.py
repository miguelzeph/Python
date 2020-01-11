import urllib.request
import json 
from pprint import pprint

url= 'http://pt.wikipedia.org/wiki/Anexo:Lista_de_filmes_de_terror'
request = urllib.request.Request(url)
resp = urllib.request.urlopen(url).read()
#data = json.loads(resp.decode('UTF-8'))

pprint(resp['tittle'])

#classes 
#pprint(data['type'])
#pprint(data['value']['categories'])
#pprint(data['value']['joke'])