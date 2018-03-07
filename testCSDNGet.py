import urllib.request

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                            "Chrome/64.0.3282.186 Safari/537.36"}
localFile = "D:\\Python\\练习\\CSDNSpider\\CSDNFile\\loginPage.html"

opener=urllib.request.build_opener()
opener.addheaders=[header]
urllib.request.install_opener(opener)
a="http://my.csdn.net/"
#urllib.request.urlretrieve(a, filename=localFile)
data=urllib.request.urlopen(a).read().decode("utf-8","ignore")
print(data)