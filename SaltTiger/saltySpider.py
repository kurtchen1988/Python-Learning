from urllib import request,parse
import re, random, time
from lxml import etree

indexURL = 'https://salttiger.com/'
userAgent = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586',
'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0)',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 BIDUBrowser/8.3 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.9.2.1000 Chrome/39.0.2146.0 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36 Core/1.47.277.400 QQBrowser/9.4.7658.400',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 UBrowser/5.6.12150.8 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.154 Safari/537.36 LBBROWSER',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36 TheWorld 7',
'Mozilla/5.0 (Linux; Android 5.0; SM-N9100 Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 V1_AND_SQ_5.3.1_196_YYB_D QQ/5.3.1.2335 NetType/WIFI',
'Mozilla/5.0 (Linux; Android 5.0; SM-N9100 Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 MicroMessenger/6.0.2.56_r958800.520 NetType/WIFI',
'Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Mobile/11D257 QQ/5.2.1.302 NetType/WIFI Mem/28',
'Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Mobile/11D257 MicroMessenger/6.0.1 NetType/WIFI',]
totalPagePat = '<a class="last" href="https://salttiger.com/page/(.*?)/">最旧 »</a>'
titlePat = '<header class="entry-header">(.*?)</header>'
itemPat = '<article.*>'
htmlHead = '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Title</title></head><body>'
htmlFoot = '</body></html>'

def getUA():
    return {'User-Agent':random.choice(userAgent)}

def getTotals():
    try:
        req = request.Request(indexURL,headers=getUA())
        html = request.urlopen(req)
        page = html.read().decode('utf-8')
        totals = re.findall(totalPagePat,page)
        return totals[0]
    except Exception as err:
        print(err)


def getPages(pageNum):
    pageURL = indexURL + "page/"+str(pageNum)
    req = request.Request(pageURL, headers=getUA())
    html = request.urlopen(req)
    page = html.read().decode('utf-8')
    #item = re.findall(itemPat, page)
    return page

def getItem(data):
    #item = re.findall(itemPat,data)
    treedata = etree.HTML(data)
    item = treedata.xpath("//article")
    return item

def writeToFile(key):
    try:
        stamp = time.strftime('%Y-%m-%d%H%M%S', time.localtime(time.time()))
        file = open('./book'+stamp+'.html','w+',encoding='utf-8')
        file.write(htmlHead)
        if key == 'all':
            for i in range(1,int(getTotals())+1):
                for content in getItem(getPages(i)):
                    html = etree.tostring(content)
                    file.write(html.decode("utf-8"))
        else:
            for i in range(1, int(key)+1):
                for content in getItem(getPages(i)):
                    html = etree.tostring(content)
                    file.write(html.decode("utf-8"))
        file.write(htmlFoot)
        file.close()
    except Exception as err:
        print(err)

def mainControl():
    pass

if __name__ == "__main__":
    i = input("请输入想要抓取的页数并回车（从第一页至第几页），如果想抓取所有数据，请输入all")
    writeToFile(i)
    print("爬取完成！")