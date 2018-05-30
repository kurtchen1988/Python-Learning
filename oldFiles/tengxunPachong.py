#1，腾讯视频评论爬虫（单页评论爬虫）：获取深度解读
import urllib.request
import re
#https://video.coral.qq.com/filmreviewr/c/upcomment/[视频ID]?&commentid=[评论ID]&reqnum=[每次提取的评论的个数]
vid="j6cgzhtkuonf6te"
cid="6231889989812701737"
#从第一个先开始
num="20"
#提取20条数据
url="https://video.coral.qq.com/filmreviewr/c/upcomment/"+vid+"?&commentid="+cid+"&reqnum="+num
#构造当前评论网址按照之前的url格式
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36",
         "Content-Type":"application/json; charset=UTF-8"}
#设置用户代理，这里可以放置其它内容，不仅仅是User-Agent
opener=urllib.request.build_opener()
headall=[]
for key,value in headers.items():
    item=(key,value)
    headall.append(item)
opener.addheaders=headall
urllib.request.install_opener(opener)
for j in range(0,100):
#抓取100次
    print("第"+str(j)+"页")
    #爬取当前评论页面
    thisurl="https://video.coral.qq.com/filmreviewr/c/upcomment/"+vid+"?&commentid="+cid+"&reqnum="+num
    data=urllib.request.urlopen(thisurl).read().decode("utf-8")
    titlepat='"title":"(.*?)","abstract":"'
    #标题的正则,抓取的时候光用标题关键字不够，需要用标题后面的abstract
    commentpat='"content":"(.*?)"'
    #评论内容的正则
    titleall=re.compile(titlepat,re.S).findall(data)
    commentall=re.compile(commentpat,re.S).findall(data)
    lastpat='"last":"(.*?)"'
    #得到下一页id的正则表达
    cid=re.compile(lastpat,re.S).findall(data)[0]
    for i in range(0,len(titleall)):
        try:
            print("评论标题是："+eval('u"'+titleall[i]+'"'))
            print("评论内容是：" + eval('u"' + commentall[i] + '"'))
            print("----------")
        except Exception as err:
            print(err)