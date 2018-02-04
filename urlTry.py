import urllib.request
for i in range(0,100):
    file=urllib.request.urlopen("http://yum.iqianyue.com",timeout=1)
    try:
        print(file.read.decode("UTF-8"))
    except Exception as err:
        print("error")