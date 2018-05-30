import urllib.request
#urlretrieve(网址，本地文件存储地址)直接下载网页到本地
urllib.request.urlretrieve("http://www.baidu.com","D:\Python\练习\iofile\download.html")
#urlcleanup()清除缓存
urllib.request.urlcleanup()
#看相应的简介信息info()
file=urllib.request.urlopen("https://read.douban.com/provider/all")
print(file.info())
#返回网页爬取的状态码getcode()可以用来测试网页的状态，如果没有返回200，那么就是有问题
print(file.getcode())
#获取当前访问的网页的url，geturl()
print(file.geturl())

