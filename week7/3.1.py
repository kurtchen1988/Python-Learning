import urllib3
import re

url = "http://www.baidu.com"

http = urllib3.PoolManager()

res = http.request("GET", url)

print("status:%d" % res.status)

data = res.data.decode("utf-8")

print(re.findall("<title>(.*?)</title>", data))