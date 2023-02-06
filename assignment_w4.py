import urllib.request, urllib.error
from bs4 import BeautifulSoup
import ssl

# fhand = urllib.request.urlopen()
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = 'http://py4e-data.dr-chuck.net/comments_1430646.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
Sum = 0

tags = soup('span')
for tag in tags:
    # print(type(int(tag.contents[0])))
    Sum = Sum + int(tag.contents[0])
    # Look at the parts of a tag
    # print ('TAG:',tag)
    # print ('URL:',tag.get('href', None))
    # print ('Contents:',tag.contents[0])
    # print ('Attrs:',tag.attrs)
    # break

# for line in html:
#     Sum = Sum + line
print('Total = ', Sum)


