import re
import urllib.request
import datetime
import time

class getCSDNContent():

    url="http://blog.csdn.net/"
    #爬取的URL网址
    pat='<a strategy=".*" href="(http://blog.csdn.net/.*)" target="_blank">'
    #正则表达式
    folder="folder"
    #存储抓取文件的路径

    def getContent(self):
    #抓取网页内容
        try:
            a=urllib.request.urlopen(self.url).read().decode("utf-8")
        except urllib.error.URLError as err:
            print(err)
        return a

    def filterContent(self):
    #通过内容获取网址
        a=self.getContent()
        b=list(set(re.compile(self.pat).findall(a)))
        return b

    def saveContent(self,folder):
    #存储获取内容
        self.folder=folder
        n=1
        if (len(self.filterContent()) == 0):
            print("未能抓取任何网页信息")
        else:
            for i in self.filterContent():
                try:
                    urllib.request.urlretrieve(i, folder+"csdn"+str(n)+".html")
                    n+=1
                except urllib.error.URLError as err:
                    print(err)

    def scheTime(self,hour,min,wait,folder):
        while True:
            now=datetime.datetime.now()
            if now.hour==hour and now.minute==min:
                break
            time.sleep(wait)
        self.saveContent(folder)

if __name__ == "__main__":
    print("请输入抓取任务开始的小时：")
    a=input()
    print("请输入抓取任务开始的分钟：")
    b=input()
    print("请输入系统检查间隔时间（以秒为单位）：")
    c=input()
    print("请输入文件夹目录（注意文件夹分隔符用/）：")
    d=input()
    getCSDNContent().scheTime(int(a),int(b),int(c),str(d))