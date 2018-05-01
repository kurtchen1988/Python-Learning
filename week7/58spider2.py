import requests
import re

data = {'key':'python','final':1,'jump':1}
url ="http://bj.58.com/job/?key=java&final=1&jump=1"
req = requests.get(url,params=data)

html = req.content.decode("utf-8")

#html = res.read().decode("utf-8")

#print(len(html))

pat = '<span class="address">(.*?)</span> | <span class="name">(.*?)</span>'
dlist = re.findall(pat,html)

#print(len(dlist))

for v in dlist:
    print(v[0]+":"+v[1])