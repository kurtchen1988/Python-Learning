#超时设置
import urllib.request
for i in range(0,100):
    try:
        file=urllib.request.urlopen("http://www.baidu.com",timeout=1)#timeout是超时的时间，秒数
        print(len(file.read().decode("UTF-8")))
    except Exception as err:
        print("error"+str(err))
