import urllib
import urllib.error
import urllib.request

try:
    site = urllib.request.urlopen('https://freebitco.in/?op=home')
except urllib.error.URLError:
    print('O site Nao esta acessivel no momento.')
else:
    print('O site esta online e foi acessado')
