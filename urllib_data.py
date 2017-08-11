# To pass data to basic url to get source code of different pages of that website, eg:- http://pythonprogramming.net/?s=basics&submit=Search from http://pythonprogramming.net

import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import urllib.request
import urllib.parse
url="http://pythonprogramming.net"
values={'s':'basic','submit':'search'}
data=urllib.parse.urlencode(values)
data=data.encode('utf-8')
req=urllib.request.Request(url,data)
resp=urllib.request.urlopen(req)
respData=resp.read()
print(respData)
