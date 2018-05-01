import urllib.request
import re
#url="http://www.baidu.com"
url = "http://www.csdn.net"
res = urllib.request.urlopen(url)
#print(res.read().decode("utf-8"))
pat = re.compile("<title>(.*?)</title>")
out = re.findall(pat,res.read().decode('utf-8'))
print(out)