import urllib.request
import re
url = "http://news.baidu.com/"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}
req = urllib.request.Request(url, headers=headers)
res = urllib.request.urlopen(req)

html = res.read().decode("utf-8")

#print(len(html))

pat = '<a href="(.*?)" .*? target="_blank">(.*?)</a>'
dlist = re.findall(pat,html)

for v in dlist:
    print(v[0]+":"+v[1])