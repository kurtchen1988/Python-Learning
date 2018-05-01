import re

f = open("./index.html","r", encoding="utf-8")
content = f.read()
f.close()

#print(content)

dlist = re.findall("<li><a href=\".*?\">.*?</a></li>", content)

#print(dlist)

for v in dlist:
    print(v[1]+":"+v[0])