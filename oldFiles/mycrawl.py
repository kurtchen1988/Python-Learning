import redis
import pymysql
import urllib.request
import re
rconn=redis.Redis("172.17.0.7","6379")
#url:http://www.17k.com/book/1.html
'''
在redis中创建值，url对应结果
url-i-"1"
'''

for i in range(0,50000):
#判断当前构建网址是否存在：
    isdo=rconn.hget("url",str(i))
    #从redis数据库取出，如果能拿到值，就证明已经爬取过，就跳过
    if(isdo!=None):
        continue
    rconn.hset("url",str(i),"1")
    #将未爬取的数据写入redis数据库
    try:
        data=urllib.request.urlopen("http://www.17k.com/book/"+str(i)+".html").read().decode("utf-8","ignore")
    except Exception as err:
        print(str(i)+str(err))
        continue
    pat='<a class="red" href=".*?">(.*?)</a>'
    rst=re.compile(pat,re.S).findall(data)
    if(len(rst)==0):
        continue
    name=rst[0]
    rconn.hset("rst",str(i),str(name))