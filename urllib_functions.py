# reading source code of google.com
import urllib.request
x = urllib.request.urlopen("http://www.google.com")
print(x.read())

# getting http status of google.com
import urllib.request
x = urllib.request.urlopen("http://www.google.com")
print(x.code)


# to get info regarding charset etc of google.com
import urllib.request
x = urllib.request.urlopen("http://www.google.com")
print(x.info())
