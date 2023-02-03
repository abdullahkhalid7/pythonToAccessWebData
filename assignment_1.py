import re
fsum = 0
fh = open('regex_sum_1430644.txt')
for line in fh:
    x = re.findall('[0-9]+', line)
    if x:
        for y in x:
            # print(type(y))
            z = int(y)
            # print(type(z))
            fsum = fsum + z

print(fsum)
