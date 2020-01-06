import urllib2

url = "http://www.google.com"

request = urllib2.Request(url)
response = urllib2.urlopen(request)
document = response.read()
print document