from requests.exceptions import RequestException
from lxml import etree
from bs4 import BeautifulSoup
from pyquery import PyQuery
import requests
import time,json

def getPage(url):
    '''爬取指定url地址的信息'''
    try:
        #定义请求头信息
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'}
        #执行爬取
        res = requests.get(url,headers=headers)
        #判断并返回结果
        if res.status_code == 200:
            return res.text
        else:
            return None
    except RequestException:
        return None

def parsePage(content):
    '''解析爬取网页中内容，并返回结果'''
    #print(content)
    #========使用pyquery解析======================
    #初始化，返回Pyquery对象
    doc = PyQuery(content)
    #解析网页中<div class="item">....</div>信息（一部部电影信息）
    items = doc("div.item")
    #遍历并解析每部电影具体信息
    for item in items.items():
        yield {
            'index':item.find('div.pic em').text(),
            'title':item.find("div.hd span.title").text(),
            'image':item.find("div.pic img").attr('src'),
            'actor':item.find("div.bd p:eq(0)").text(),
            'score':item.find("div.star span.rating_num").text(),
        }
    '''
    #========使用BeautifulSoup解析======================
    #初始化，返回BeautifulSoup对象
    soup = BeautifulSoup(content,'lxml')
    #解析网页中<div class="item">....</div>信息（一部部电影信息）
    items = soup.find_all(name="div",attrs={"class":"item"})
    #遍历并解析每部电影具体信息
    for item in items:
        yield {
            'index':item.em.string,
            'title':item.find(name="span",attrs={'class':'title'}).string,
            'image':item.find(name="img",attrs={'width':'100'}).attrs['src'],
            'actor':item.select("div.bd p")[0].get_text(),
            'score':item.select("div.star span.rating_num")[0].string,
        }
    '''
    '''
    #========使用Xpath解析======================
    #初始化，返回根节点对象
    html = etree.HTML(content)
    #解析网页中<div class="item">....</div>信息（一部部电影信息）
    items = html.xpath("//div[@class='item']")
    #遍历并解析每部电影具体信息
    for item in items:
        yield {
            'index':item.xpath(".//div/em[@class='']/text()")[0],
            'title':item.xpath(".//span[@class='title']/text()")[0],
            'image':item.xpath(".//img[@width='100']/@src")[0],
            'actor':item.xpath(".//p[@class='']/text()")[0],
            'score':item.xpath(".//span[@class='rating_num']/text()")[0],
        }
    '''

def writeFile(content):
    '''解析爬取网页中内容，并返回结果'''
    with open("./result.txt",'a',encoding="utf-8") as f:
        f.write(json.dumps(content,ensure_ascii=False)+"\n")

def main(offset):
    '''主程序函数，负责调度执行爬取处理'''
    url = 'https://movie.douban.com/top250?start='+str(offset)
    html = getPage(url) #执行爬取
    if html:
        for item in parsePage(html): #执行解析并遍历
            print(item)
            writeFile(item) #执行写操作

#判断当前执行是否为主程序，并遍历调度主函数来爬取信息
if __name__ == '__main__':
    main(0)
    #for i in range(10):
    #    main(offset=i*25)
    #    time.sleep(1)