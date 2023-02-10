import urllib.request
import urllib.error
import xml.etree.ElementTree as Et
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = 'http://py4e-data.dr-chuck.net/comments_1430648.xml'
web = urllib.request.urlopen(url, context=ctx).read().decode()
stuff = Et.fromstring(web)
lst = stuff.findall('comments/comment')
sm = 0
for item in lst:
    sm = sm + int(item.findtext('count'))
print('Total: ', sm)
