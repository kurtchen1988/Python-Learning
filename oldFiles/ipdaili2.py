#IP代理池实现的第二种方式(接口调用法，这种方法更适用于代理IP不稳定的情况)
import urllib.request
def ip(time,isurllib):
    if(isurllib==1):
        print("这一次调用了接口")
        thisall=urllib.request.urlopen("http://tvp.daxiangdaili.com/ip/?tid=555850358533092&num=10&foreign=only")
        ippools=[]
        for item in thisall:
            ippools.append(item.decode("utf-8","ignore"))
    else:
        print("这一次没有调用接口")
    print("当前的所有IP列表是：")
    print(ippools)
    thisip=ippools[time]
    print(ippools[time])
    proxy=urllib.request.ProxyHandler({"http":thisip})#字典形势，http对应ip
    opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    
x=0

for i in range(0,35):
    try:
        if(x%10==0):
            time=x%10
            ip(time,1)
        else:
            ip(time,0)
        url="http://www.baidu.com"
        data1=urllib.request.urlopen(url).read()
        data=data1.decode("utf-8","ignore")
        print(len(data))
        fh=open("D:\\Python\\练习\\iofile\\ip_baidu"+str(i)+".html","wb")#未解码的数据可以以wb的方式写入，二进制
        fh.write(data1)
        fh.close()
        x+=1
    except Exception as err:
        print(err)
        x+=1
