from lxml import etree
from bs4 import BeautifulSoup
from requests import RequestException
import requests, random, re, json,os
from pyquery import PyQuery
from urllib.parse import urlencode
from urllib.request import urlretrieve

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
    用PyQuery方法处理豆瓣图书数据
    :param content: 网页内容
    :return: 带有相应信息的字典
    '''
    html = PyQuery(content)
    items = html("tr.item")

    for item in items.items():
        a = item.find('a.nbg').attr('onclick')
        print(a)
        print(item.find('p:eq(0)').text())
        yield {
            'rank': str(int(re.findall("moreurl\(this,{i:'(.*?)'}\)",a)[0])+1),
            'pic': item.find('a').attr('href'),
            'name': item.find('div a').attr('title'),
            'mark': item.find('span.rating_nums').text(),
            'author': item.find('p:eq(0)').text(),
        }


def parsePageXP(content):
    '''
    用XPath方法处理豆瓣图书数据
    :param content: 网页内容
    :return: 带有相应信息的字典
    '''
    html = etree.HTML(content)
    items = html.xpath('//table/tr')
    #print(items)
    for item in items:
        a=item.xpath('.//a[@class="nbg"]/@onclick')
        print(item.xpath('.//img[@width="90"]/@src'))

        yield {
            'rank': str(int(re.findall("moreurl\(this,{i:'(.*?)'}\)",a[0])[0])+1),
            'pic': item.xpath('.//img[@width="90"]/@src')[0],
            'name': item.xpath('.//div/a/@title')[0],
            'mark': item.xpath('.//span[@class="rating_nums"]/text()')[0],
            'author' : item.xpath('//p/text()')[2],
        }



def parsePageBS(content):
    '''
    用BeautifulSoup方法处理豆瓣图书数据
    :param content: 网页内容
    :return: 带有相应信息的字典
    '''
    html = BeautifulSoup(content,'lxml')
    items = html.find_all(name="tr", attrs={"class":"item"})

    for item in items:
        a = item.find(name="a",attrs={'class':'nbg'}).attrs['onclick']

        yield {
            'rank': str(int(re.findall("moreurl\(this,{i:'(.*?)'}\)",a)[0])+1),#测试这个的问题
            'pic': item.find(name="img", attrs={'width':'90'}).attrs['src'],
            'name': item.find(name="a", attrs={'title': True}).attrs['title'],
            'mark': item.select('span.rating_nums')[0].string,
            'author': item.find(name="p", attrs={"class":True}).string,
        }


def writeFile(content):
    '''
    解析爬取网页中内容，并返回结果
    :param content: 网页代码
    :return: None
    '''
    with open("./result.txt",'a',encoding="utf-8") as f:
        f.write(json.dumps(content,ensure_ascii=False)+"\n")

def bookMain(offset, option):
    '''

    :param offset: 选择爬取的页数
    :param option: 选择解析的方法
    :return:
    '''
    for i in range(0,offset+1):
        url = 'https://book.douban.com/top250?start='+str(offset)
        html = getPage(url) #执行爬取
        if html:
            if(option=='1'):
                for item in parsePageXP(html): #执行解析并遍历
                    print(item)
                    writeFile(item) #执行写操作
            elif(option=='2'):
                for item in parsePageBS(html): #执行解析并遍历
                    print(item)
                    writeFile(item) #执行写操作
            elif(option=='3'):
                for item in parsePagePY(html): #执行解析并遍历
                    print(item)
                    writeFile(item) #执行写操作


def showCart():
    '''
    京东购物车爬虫。通过对cookie等处理，爬取其商品描述与价格，并打印出来。用BeautifulSoup筛选数据
    :return: None
    '''
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

def getImgPage(offset):
    '''
    处理网页数据，将处理好带有图片url信息的字典返回。首先将带有页数信息的参数传入网页，将返回信息筛选，有效信息返回。
    :param offset: 需要爬取的页数
    :return: 带有图片url信息的字典
    '''
    params = []
    for i in range(30, 30 * offset + 30, 30):
        params.append({
            'tn': 'resultjson_com',
            'ipn': 'rj',
            'ct': 201326592,
            'is': '',
            'fp': 'result',
            'queryWord': '街拍',
            'cl': 2,
            'lm': -1,
            'ie': 'utf-8',
            'oe': 'utf-8',
            'adpicid': '',
            'st': -1,
            'z': '',
            'ic': 0,
            'word': '街拍',
            's': '',
            'se': '',
            'tab': '',
            'width': '',
            'height': '',
            'face': 0,
            'istype': 2,
            'qc': '',
            'nc': 1,
            'fr': '',
            'pn': i,
            'rn': 30,
            'gsm': '1e',
            '1488942260214': ''
        })
    url = 'https://image.baidu.com/search/acjson'
    urls = []
    for i in params:
        urls.append(requests.get(url, params=i).json().get('data'))

    return urls


def saveImage(item):
    '''
    保存图片于程序根目录下的mypic文件夹中。如果mypic文件夹不存在，建立此文件夹。通过遍历参数传递过来的字典，取得其中url
    的值，并用urlretrieve方法将其存下来。
    :param item: 带有url信息的字典
    :return: None
    '''
    path = "./mypic/"
    if not os.path.exists(path):  # 如果文件夹不存在新建文件夹
        os.mkdir(path)

    x = 0
    for list in item:
        for i in list:
            if i.get('thumbURL') != None:
                urlretrieve(i.get('thumbURL'),path+str(x)+'.jpg')
                x += 1
            else:
                print('图片链接不存在')

    print("爬取完成，图片已存在根目录下mypic文件夹")


if __name__ == '__main__':
    '''主入口程序，简单的GUI界面让用户简单使用程序'''
    x=True
    while x==True:
        print("欢迎使用爬虫程序，请选择需要使用的功能\n")
        print("1. 豆瓣图书TOP250爬虫\n")
        print("2. 京东购物车爬虫\n")
        print("3. 百度图片街拍爬虫\n")
        print("请选择（q键为退出键）")
        a=input()
        if a=='1':
            print("请选择爬取方式：\n")
            print("1. Xpath爬取\n")
            print("2. BeautifulSoup爬取\n")
            print("3. PyQuery爬取\n")
            b=input()
            print("请选择爬取的页数：\n")
            c=input()
            bookMain(int(c),b)
        elif a=='2':
            showCart()
        elif a=='3':
            print("请选择想要爬取的页数（每页30张图片）")
            a=input()
            saveImage(getImgPage(int(a)))
        elif a=='q':
            x=False