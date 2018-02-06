#get请求实战--实现百度信息自动搜索
import urllib.request
import re
keywd="中文"
keywd=urllib.request.quote(keywd)
#page=(num-1)*10
for i in range(1,11):
    url="http://www.baidu.com/s?wd="+keywd+"&pn="+str((i-1)*10)
    data=urllib.request.urlopen(url).read().decode("utf-8")
    pat="title:'(.*?)',"
    pat2='title":"(.*?)",'
    rst=re.compile(pat).findall(data)
    rst2=re.compile(pat2).findall(data)
    for j in range(0,len(rst)):
        print(rst[j])
    for z in range(0,len(rst2)):
        print(rst2[z])
    #print(rst)
    #print(rst2)
