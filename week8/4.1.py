import requests
import re

url = "https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv3358&productId=7348367&score=0&sortType=5&page=1&pageSize=10&isShadowSku=0&rid=0&fold=1"

res = requests.get(url)

html = res.text

pat = '"content":"(.*?)"'

items = re.findall(pat, html, re.S)

for v in items:
    print(v)
    print("="*60)