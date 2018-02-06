#爬取腾讯新闻首页所有新闻内容
'''
1，爬取新闻首页
2，得到各新闻链接
3，爬取新闻链接
4，寻找有没有frame
5，若有，抓取frame下对应网页内容
6，若没有，直接抓取当前网页内容
'''

import urllib.request
import re

url="https://news.qq.com/"
data=urllib.request.urlopen(url).read().decode("UTF-8","ignore")
pat1='<a target="_blank" class="linkto" href="(.*?)"'
alllink=re.compile(pat1).findall(data)
