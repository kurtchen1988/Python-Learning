#IP代理的构建
import urllib.request
#ip代理失效时间非常短，尽快应用
ip="125.40.16.233:8118"
#把代理IP转换成相应格式，可以应用到opener中
#代理IP的使用方式
proxy=urllib.request.ProxyHandler({"http":ip})#字典形势，http对应ip
opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
urllib.request.install_opener(opener)
url="http://www.baidu.com"
data1=urllib.request.urlopen(url).read()
data=data1.decode("utf-8","ignore")
print(len(data))
fh=open("D:\\Python\\练习\\iofile\\ip_baidu.html","wb")#未解码的数据可以以wb的方式写入，二进制
fh.write(data1)
fh.close()
