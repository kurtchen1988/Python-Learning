import urllib, re
from urllib import request, parse
import requests, json, random



youdaoURL = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
tongchenURL = 'http://bj.58.com/dashanzi/chuzu/pn'
movieURL = 'http://maoyan.com/board/4?offset=0'
titlePat = 'rel="nofollow" >(.*?)</a>'
picPat = ''
typePat = ''
pricePat = ''
# 【标题、图片、户型、价格】

#【序号、图片、电影名称、主演、时间、评分】

def youdaoRe(keyword):

    trans = {'i': keyword,
        'doctype': 'json',}

    res = requests.post(youdaoURL, data=trans)
    str_json = res.content.decode("utf-8")
    myjson = json.loads(str_json)

    print("翻译结果："+myjson['translateResult'][0][0]['tgt'])

def youdaoUR(keyword):

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
    while True:
        keyword = input("请输入要翻译词：")
        if keyword == 'q':
            break
        youdaoRe(keyword)

def getyoudaoUR():
    while True:
        keyword = input("请输入要翻译词：")
        if keyword == 'q':
            break
        youdaoUR(keyword)


def gettongcheng(page):
    res = request.urlopen(tongchenURL+str(page)+'/')
    html = res.read().decode('utf-8')
    print(re.findall(titlePat,html))
    pass

if __name__ == "__main__":
    gettongcheng(1)