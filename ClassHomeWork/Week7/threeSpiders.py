import urllib, re
from urllib import request, parse
import requests, json, random



youdaoURL = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
# 有道翻译url
tongchenURL = 'http://bj.58.com/dashanzi/chuzu/pn'
# 58同城租房url
movieURL = 'http://maoyan.com/board/4?offset='
# 猫眼电影url
titlePat = 'tongji.*\n.*\n.*?>\n\s*(.*?)\s*</a>'
# 58同城租房标题正则
picPat = 'lazy_src="(.*?)"'
# 58同城租房图片正则
typePat = '<p class="room">(.*?)\s*&nbsp;'
# 58同城租房户型正则
pricePat = '<div class="money">\s*<b>(.*?)\s*</div>'
# 58同城租房价格正则
removePrice = '</b>'
# 58同城租房移除价格中标签的正则
serialPat = '<i class="board-index board-index-\d*">(.*?)</i>'
# 猫眼电影序号正则
moPicPat = '<img src="(.*?)" alt="" class="poster-default" />'
# 猫眼电影图片正则
moNamePat = '<p class="name"><a href="/films/.*?" title=".*?" data-act="boarditem-click" data-val="{movieId:.*?}">(.*?)</a></p>'
# 猫眼电影电影名称正则
starPat = '<p class="star">\s*(.*?)\s*</p>'
# 猫眼电影主演正则
timePat = '<p class="releasetime">(.*?)</p>'
# 猫眼电影时间正则
rateIntPat = '<i class="integer">(.*?)</i>'
# 猫眼电影评分整数位正则
rateFrapat = '<i class="fraction">(.*?)</i>'
# 猫眼电影评分小数位正则

def youdaoRe(keyword):
    '''用requests方式爬取有道字典信息，keyword参数为输入的信息'''
    trans = {'i': keyword,
        'doctype': 'json',}

    res = requests.post(youdaoURL, data=trans)
    str_json = res.content.decode("utf-8")
    myjson = json.loads(str_json)

    print("翻译结果："+myjson['translateResult'][0][0]['tgt'])

def youdaoUR(keyword):
    '''用urllib方法爬取有道字典信息，keyword参数为输入的信息'''
    trans = {'i': keyword,
             'doctype': 'json', }

    data = parse.urlencode(trans)
    req = request.Request(youdaoURL, data=bytes(data, encoding='utf-8'))
    res = request.urlopen(req)

    str_json = res.read().decode("utf-8")
    # print(str_json)
    myjson = json.loads(str_json)

    print("翻译结果：" + myjson['translateResult'][0][0]['tgt'])


def getyoudaoRe():
    '''requests爬取有道字典控制方法'''
    while True:
        keyword = input("请输入要翻译词：")
        if keyword == 'q':
            break
        youdaoRe(keyword)

def getyoudaoUR():
    '''urllib爬取有道字典控制方法'''
    while True:
        keyword = input("请输入要翻译词：")
        if keyword == 'q':
            break
        youdaoUR(keyword)


def gettongcheng(page):
    '''爬取58同城租房信息，参数page为第几页'''
    res = request.urlopen(tongchenURL+str(page)+'/')
    html = res.read().decode('utf-8')
    title = re.findall(titlePat,html)
    pic = re.findall(picPat, html)
    type = re.findall(typePat, html)
    price = re.findall(pricePat, html)
    for i in range(0, len(title)):
        print("【"+title[i]+"、"+pic[i]+"、"+type[i]+"、"+re.sub(removePrice,' ',price[i])+"】")
    pass

def getmovie():
    '''爬取猫眼电影方法'''
    for i in range(0,100,10):
        res = request.urlopen(movieURL + str(i))
        html = res.read().decode('utf-8')
        serial = re.findall(serialPat, html)
        pic = re.findall(moPicPat, html)
        type = re.findall(moNamePat, html)
        star = re.findall(starPat, html)
        time = re.findall(timePat, html)
        rateInt = re.findall(rateIntPat, html)
        rateFra = re.findall(rateFrapat, html)
        for n in range(0, len(serial)):
            print("【" + serial[n] + "、" + pic[n] + "、" + type[n] + "、" + star[n] + "、" + time[n] + "、" + rateInt[n]+rateFra[n] + "】")


if __name__ == "__main__":
    '''程序入口方法，q键为退出。在爬取有道字典中，q键返回到前页面'''
    while True:
        print("欢迎使用爬虫程序，请选择功能：\n")
        print("1. 用urllib方法爬取有道字典\n")
        print("2. 用requests方法爬取有道字典\n")
        print("3. 爬取58同城租房信息\n")
        print("4. 爬取猫眼电影\n")
        keyinput = input("请选择：")
        if(keyinput=='1'):
            getyoudaoRe()
        elif(keyinput=='2'):
            getyoudaoUR()
        elif(keyinput=='3'):
            pageinput = input("请输入要爬取的页数：")
            gettongcheng(pageinput)
        elif(keyinput=='4'):
            getmovie()
        elif(keyinput=='q'):
            break