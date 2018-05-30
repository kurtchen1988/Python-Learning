#糗事百科段子爬虫
import urllib.request
import re
url="https://www.qiushibaike.com/8hr/page/2/"
headers=("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36")
opener=urllib.request.build_opener()
opener.addheaders=[headers]
urllib.request.install_opener(opener)
for i in range(0,35):
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
