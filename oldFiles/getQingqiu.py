#post请求实战
import urllib.request
#设置表单内容，需要转码，依赖以下的码
import urllib.parse
posturl="http://www.iqianyue.com/mypost/"
postdata=urllib.parse.urlencode({
    "name":"ceo@txk7.com",
    "pass":"adfasdfsdfwe"
    }).encode("utf-8")#括号里用字典的格式，key:value，key是name的值，同理，pass就是pass
#进行post，就需要使用urllib.request下面的Request(真实post地址，post数据）
req=urllib.request.Request(posturl,postdata)
rst=urllib.request.urlopen(req).read().decode("utf-8")
fh=open("D:/Python/练习/iofile/post.html","w")
fh.write(rst)
fh.close()
