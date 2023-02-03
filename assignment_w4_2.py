import urllib.request, urllib.error
from bs4 import BeautifulSoup
import ssl

url = input("Enter URL: ")
count = int(input("Enter count: "))
pos = int(input("Enter position: "))

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
i = 0
tags = soup('a')
while count > 0:
    for tag in tags:
        i = i + 1
        if i == pos:
            break
    print(i, 'Contents:',tag.contents[0])
    print('URL:',tag.get('href', None))
    url = tag.get('href', None)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    i = 0
    count = count - 1
