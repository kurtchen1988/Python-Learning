import re

'''
str = '<ul>\<li>aaaa</li>\<li>bbbb</li>\<li>cccc</li>\<li>dddd</li>\</ul>'

data = re.findall("<li>(.*?)</li>",str)

for v in data:
    print(v)
'''
'''
s = "12,35;42:34,56:20"
dd = re.split("[^0-9]",s)
for v in dd:
    print(v)
'''

s = "12,35;42:34,56:20"

b = re.subn("[^0-9]"," ",s)

print(b)