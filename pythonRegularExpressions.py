import re


# x = '<span class="a-size-medium a-color-base a-text-normal">Thermaltake Toughpower GX2 80+ Gold 600W SLI/Crossfire Ready Continuous Power ATX 12V V2.4/EPS V2.92 Non Modular Power Supply 5 Year Warranty PS-TPD-0600NNFAGU-2</span>'
# y = re.findall('>(.+)<', x)
# print(y)

# x = '<p>Please click <a href="http://www.dr-chuck.com">here</a></p>'
# y = re.findall('href="(.+)"',x)
# print(y)
#
# x = 'my favorite 2 numbers are 19 and 24'
# y = re.findall('[0-9]+', x)
# print(y)
# y = re.findall('[aeiou]+', x)
# print(y)
#
# # This is the greedy method the '.' and '+' regular expression goes as far as possible
# x = 'From: using the : character'
# y = re.findall('^F.+:', x)
# print(y)
#
# # Now we can make the above code non-greedy by
# y = re.findall('^F.+?:', x)
# print(y)
#
# x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# y = re.findall('@([^ ]*)', x)
# print(y)
