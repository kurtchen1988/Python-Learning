#CSDN博文爬虫
import urllib.request
import re
url="http://blog.csdn.net/"
headers=("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36")
opener=urllib.request.build_opener()
opener.addheaders=[headers]
#安装为全局
urllib.request.install_opener(opener)
data=urllib.request.urlopen(url).read().decode("utf-8","ignore")
pat='<a strategy=".*" href="(http://blog.csdn.net/.*)" target="_blank">'
alllink=re.compile(pat).findall(data)
#print(alllink)
for i in range(0,len(alllink)):
    localpath="D:\\Python\\练习\\iofile\\"
    thislink=alllink[i]
    urllib.request.urlretrieve(thislink,filename=localpath)
    print("当前文章(第"+str(i)+"篇)爬取成功"
