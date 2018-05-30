#用户代理池的构建
import urllib.request
import re
import random
uapools=[
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36",
    "User-Agent:Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0"
    "User-Agent:Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)"
    ]
#写一个方法选择随机的一个用户代理

def ua(uapools):
    thisua=random.choice(uapools)
    print(thisua)
    headers=("User-Agent",thisua)
    opener=urllib.request.build_opener()
    opener.addheaders=[headers]
    urllib.request.install_opener(opener)

for i in range(0,35):
    ua(uapools)
    #网址构造的研究，研究它的规律
    thisurl="https://www.qiushibaike.com/8hr/page/"+str(i+1)+"/"
    data=urllib.request.urlopen(thisurl).read().decode("utf-8")
    pat='<div class="content">.*?<span>(.*?)</span>.*?</div>'
    #re.S是模式修正符
    rst=re.compile(pat,re.S).findall(data)
    print(rst)
    for j in rst:
        print(j)
        print("---------")
