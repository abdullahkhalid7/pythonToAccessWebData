import urllib.request
import urllib.error
url = input("Enter - ")
'''
'http://data.pr4e.org/intro-short.txt'
'''
fh = urllib.request.urlopen(url)
for line in fh:
    print(line.decode().strip())
