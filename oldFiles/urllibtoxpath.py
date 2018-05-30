#在urllib模块下使用xpath表达式
import urllib.request
from lxml import etree

data=urllib.request.urlopen("http://www.baidu.com").read().decode("utf-8","ignore")
treedata=etree.HTML(data)
title=treedata.xpath("//title/text()")
if(str(type(title))=="<class 'list'>"):
    pass
else:
    #iList=[i for i in range(1,10)]
    #通过这个方式可以写出一个列表，它内容为1-9的数据。
    title=[i for i in title]
print(title[0])
'''
print(len(data))
print(len(treedata))
print(type(data))
print(type(treedata))
print(type(title))
print(title)
'''
