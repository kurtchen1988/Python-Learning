# 解析所有城市信息
import requests
import re

url = 'https://cdn.heweather.com/china-city-list.txt'
res = requests.get(url)
data = res.content.decode('utf-8')

# 使用换行符拆分每条城市信息
dlist = re.split("[\n\r]+", data)

#print(len(dlist))

#for i in range(5,10):
#    print(dlist[i])

# 去除多用头信息数据
for i in range(5):
    dlist.remove(dlist[0])

print(len(dlist))

# 遍历所有城市信息
for i in range(10):
    item = re.split("[\s\|]+", dlist[i])
    print(item[1], item[2], item[3])