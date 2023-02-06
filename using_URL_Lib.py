import urllib.request, urllib.error
from bs4 import BeautifulSoup

fhand = urllib.request.urlopen('http://py4e-data.dr-chuck.net/known_by_Saranna.html')
i = 0
for line in fhand:
    i = i + 1
    print(i)
    print(line.decode().strip())
# url = 'http://dr-chuck.com/page1.htm'
# url = input('Enter - ')
# html = urllib.request.urlopen(url).read()
# soup = BeautifulSoup(html, 'html.parser')
#
# tags = soup('a')
# for tag in tags:
#     print(tag.get('href', None))

