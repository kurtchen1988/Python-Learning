#IP代理池构建的第一种方案(适合于代理IP稳定的情况)
import random
import urllib.request
ippools=[
    "61.160.212.181:808",
    "119.98.209.28:8118",
    "115.226.78.142:8118",
    "114.113.126.87:80"
    ]

def ip(ippools):
    thisip=random.choice(ippools)
    print(thisip)
    proxy=urllib.request.ProxyHandler({"http":thisip})#字典形势，http对应ip
    opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)

for i in range(0,5):
    try:
        ip(ippools)
        url="http://www.baidu.com"
        data1=urllib.request.urlopen(url).read()
        data=data1.decode("utf-8","ignore")
        print(len(data))
        fh=open("D:\\Python\\练习\\iofile\\ip_baidu"+str(i)+".html","wb")#未解码的数据可以以wb的方式写入，二进制
        fh.write(data1)
        fh.close()
    except Exception as err:
        print(err)
