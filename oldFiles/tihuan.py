import urllib.request
import re

data=urllib.request.urlopen("https://read.douban.com/provider/all").read().decode("utf-8")
pat='<div class="name">(.*?)</div>'
rst=re.compile(pat).findall(data)
a=open("D:/Python/练习/iofile/1.txt","w")
for i in range(0,len(rst)):
    a.write(rst[i]+"\n")
a.close()
