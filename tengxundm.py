import urllib.request
data=urllib.request.urlopen("http://ac.qq.com/ComicView/index/id/539443/cid/1").read().decode("utf-8","ignore")
print(len(data))
fh=open("D:/Python/练习/iofile/dm1.html", "w",encoding="utf-8")
fh.write(data)
fh.close()