#浏览器伪装
import urllib.request
url="http://blog.csdn.net"
#头文件格式header=("User-Agent",具体用户代理值)
headers=("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36")
opener=urllib.request.build_opener()
opener.addheaders=[headers]
data=opener.open(url).read()
fh=open("D:/Python/练习/iofile/csdn.html","wb")
fh.write(data)
fh.close()
#需要研究的问题(以后会讲，大家先探索)
#1，如何将opener安装为全局，让URLopen（）访问时也添加对应报头？
#2,研究一下使用Request的方式进行报头添加(不讲，自行探索研究)
