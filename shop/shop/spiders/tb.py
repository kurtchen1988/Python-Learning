# -*- coding: utf-8 -*-
import scrapy
import urllib.request
import ssl
from scrapy.http import Request
import re
from shop.items import ShopItem

class TbSpider(scrapy.Spider):
    name = 'tb'
    allowed_domains = ['taobao.com']
    start_urls = ['http://www.taobao.com/']

    def parse(self, response):
        key="坚果"
        for i in range(0,10):
            url="https://s.taobao.com/search?q="+str(key)+"@search_type=item&s="+str(44*i)
            yield Request(url=url,callback=self.page)
        pass

    def page(self, response):
        body=response.body.decode("utf-8", "ignore")
        patid='"nid":"(.*?)"'
        allid=re.compile(patid).findall(body)
        print(allid)
        for j in range(0, len(allid)):
            thisid=allid[j]
            url1="http://item.taobao.com/item.htm?id="+str(thisid)
            yield Request(url=url1, callback=self.next)

    def next(self,response):
        item=ShopItem()
        item["title"]=response.xpath("//h3[@class='tb-main-title']/@data-title").extract()
        item["link"]=response.url
        item["price"]=response.xpath("//input[@name='current_price]/@value").extract()
        patid='id=(.*?)$'
        thisid=re.compile(patid).findall(response.url)[0]
        commenturl="https://rate.taobao.com/detailCount.do?callback=jsonp100&itemId="+str(thisid)
        print(commenturl)
        ssl._create_default_https_context=ssl._create_unverified_context
        #为了避免ssl出问题
        commentdata=urllib.request.urlopen(commenturl).read().decode("utf-8","ignore")
        pat='"count":(.*?}'
        item["comment"]=re.compile(pat).findall(commentdata)
        yield item