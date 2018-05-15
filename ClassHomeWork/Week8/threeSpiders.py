import urllib.request
from lxml import etree
from bs4 import BeautifulSoup
from requests import RequestException
import requests, random, re, json
from pyquery import PyQuery

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
# 报头信息，多种用户代理可供选择

def getPage(url):
    '''
    通过网址得到网页代码
    :param url: 网址
    :return: 如果网页不响应，返回None，如果响应返回网页代码
    '''
    try:
        headers = {'User-Agent':random.choice(userAgent)}
        res=requests.get(url,headers=headers)
        if(res.status_code==200):
            return res.text
        else:
            return None
    except RequestException:
        return None


def parsePagePY(content):
    '''
    用PyQuery方法处理数据
    :param content: 网页内容
    :return: 带有相应信息的字典
    '''
    html = PyQuery(content)
    items = html("tr.item")

    for item in items.items():
        a = item.find('a.nbg').attr('onclick')

        print(item.find('p:eq(0)').text())
        yield {
            'rank': str(int(re.findall("moreurl\(this,{i:'(.*?)'}\)", a[0])[0]) + 1),
            'pic': item.find('a').attr('href'),
            'name': item.find('div a').attr('title'),
            'mark': item.find('span.rating_nums').text(),
            'author': item.find('p:eq(0)').text(),
        }


def parsePageXP(content):
    '''
    用XPath方法处理数据
    :param content: 网页内容
    :return: 带有相应信息的字典
    '''
    html = etree.HTML(content)
    items = html.xpath('//table/tr')
    #print(items)
    for item in items:
        a=item.xpath('.//a[@class="nbg"]/@onclick')

        yield {
            'rank': str(int(re.findall("moreurl\(this,{i:'(.*?)'}\)",a[0])[0])+1),
            'pic': item.xpath('.//img[width="90"]/@src')[0],
            'name': item.xpath('.//div/a/@title')[0],
            'mark': item.xpath('.//span[@class="rating_nums"]/text()')[0],
            'author' : item.xpath('//p/text()')[2],
        }



def parsePageBS(content):
    '''
    用BeautifulSoup方法处理数据
    :param content: 网页内容
    :return: 带有相应信息的字典
    '''
    html = BeautifulSoup(content,'lxml')
    items = html.find_all(name="tr", attrs={"class":"item"})

    for item in items:
        a = item.find(name="a",attrs={'class':'nbg'}).attrs['onclick']

        yield {
            'rank': str(int(re.findall("moreurl\(this,{i:'(.*?)'}\)",a[0])[0])+1),
            'pic': item.find(name="img", attrs={'width':'90'}).attrs['src'],
            'name': item.find(name="a", attrs={'title': True}).attrs['title'],
            'mark': item.select('span.rating_nums')[0].string,
            'author': item.find(name="p", attrs={"class":True}).string,
        }


def writeFile(content):
    '''解析爬取网页中内容，并返回结果'''
    with open("./result.txt",'a',encoding="utf-8") as f:
        f.write(json.dumps(content,ensure_ascii=False)+"\n")

def bookMain(offset):
    '''书爬虫主程序函数，负责调度执行爬取处理'''
    url = 'https://movie.douban.com/top250?start='+str(offset)
    html = getPage(url) #执行爬取
    if html:
        for item in parsePageBS(html): #执行解析并遍历
            print(item)
            writeFile(item) #执行写操作

def showCart():
    para = {'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'accept-encoding':'gzip, deflate, br',
            'accept-language':'zh-CN,zh;q=0.9',
            'cache-control':'max-age=0',
            'cookie':'3AB9D23F7A4B3C9B=7OJ4YCECRFKW3VVAJRUHD35I37MRKSDDNQL6BWXXQNLPEZTC37WARLSNXQLSWZIPMGLLZOQFSEHAJPO4OI3MOK6F6A; __jdv=122270672|direct|-|none|-|1525709885231; __jdu=14782404; PCSYCityID=1213; ipLoc-djd=1-72-2799-0; user-key=770bec6c-1c30-43f9-a684-a1a3fece95fc; shshshfp=131cccb7ba454e168f0b7781af85c969; shshshfpa=7c6b6cd4-3dbc-783a-9818-baeef089469e-1526388623; __jda=122270672.14782404.1521363148.1525709885.1526388624.2; __jdc=122270672; shshshfpb=211fc1ba49005430ab5029f4c14f3304c5afa060853c96c1866d9d6d93; cart-main=xx; cn=4; cd=0; __jdb=122270672.7.14782404|2.1526388624; shshshsID=a8f0a54b156bbde9fb91183f320a9aa6_4_1526388944597',
            'referer':'https://cart.jd.com/addToCart.html?rcd=1&pid=10430900577&pc=1&eb=1&rid=1526388740244&em=',
            'upgrade-insecure-requests':'1',
            'user-agent':random.choice(userAgent),}
    url = 'https://cart.jd.com/cart.action'

    response = requests.get(url,headers= para)

    html = BeautifulSoup(response.text, 'lxml')
    name = html.find_all(name='a', attrs={'clstag':'clickcart|keycount|xincart|cart_sku_name'})
    price = html.find_all(name='div', attrs={'class':'cell p-price p-price-new '})
    for i in range(0, len(name)):
        print("详细描述： "+name[i].string)
        print("价格： "+price[i].find(name='strong').string)

def picDown(page):
    pass

if __name__ == '__main__':
    html = getPage("https://book.douban.com/top250?start=0")
    showCart()
    #print(html)