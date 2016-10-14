from urllib.request import urlopen
import urllib
from urllib import *
from bs4 import BeautifulSoup

myUrl = "http://www.qiushibaike.com/hot/"
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}
req = urllib.request.Request(myUrl, headers=headers)
html = urlopen(req)
bsObj = BeautifulSoup(html, "html.parser")
nameList = bsObj.findAll("", {"class": "content"})

for name in nameList:
    print(name.get_text())

