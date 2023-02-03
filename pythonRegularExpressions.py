import re
x = '<p>Please click <a href="http://www.dr-chuck.com">here</a></p>'
y = re.findall('href="(.+)"',x)
print(y)
'''
href="(.+)"
href=".+"
http://.*
<.*>
'''


x = 'my favorite 2 numbers are 19 and 24'
y = re.findall('[0-9]+', x)
print(y)
y = re.findall('[aeiou]+', x)
print(y)

# This is the greedy method the '.' and '+' regular expression goes as far as possible
x = 'From: using the : character'
y = re.findall('^F.+:', x)
print(y)

# Now we can make the above code non-greedy by
y = re.findall('^F.+?:', x)
print(y)

x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('@([^ ]*)', x)
print(y)
