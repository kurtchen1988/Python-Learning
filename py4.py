#简单爬虫的编写
'''
import urllib.request
data=urllib.request.urlopen("https://edu.csdn.net/").read()
'''
#自动提取课程页面的qq群
import urllib.request
import re1
data=urllib.request.urlopen("https://edu.csdn.net/lecturer/1739").read().decode("utf-8")
pat="：(\d*?),"
string=re1.compile(pat).findall(data)
print(string)
