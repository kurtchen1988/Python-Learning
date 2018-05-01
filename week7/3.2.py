import requests
import re

url = "http://www.baidu.com"

res = requests.get(url)

print("status:%d" % res.status_code)

data = res.content.decode("utf-8")

print(re.findall("<title>(.*?)</title", data))