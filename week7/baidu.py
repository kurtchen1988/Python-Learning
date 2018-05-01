from urllib import request,parse
import json

url = "http://fanyi.baidu.com/sug"

data = {'kw':'你好'}
data = parse.urlencode(data)

headers = {'Content-Length':len(data)}

req = request.Request(url,data=bytes(data, encoding="utf-8"), headers=headers)
res = request.urlopen(req)

str_json = res.read().decode("utf-8")
#print(str_json)
myjson = json.loads(str_json)

print(myjson['data'][0]['v'])