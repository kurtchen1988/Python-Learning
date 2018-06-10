# -*- coding: utf-8 -*-
import scrapy, re
from scrapy import Request, Spider
from jdspider.items import JdspiderItem


class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['www.jd.com']
    base_url = 'https://list.jd.com/list.html?cat=670,671,672&page='

    def start_requests(self):
        '''
        爬虫开始方法，通过对页数参数读取，创造一个for循环，再通过yield来创建一个Request并访问parse方法
        :return: None
        '''
        for page in range(1, self.settings.get('MAX_PAGE')+1):
            url = self.base_url+str(page)
            yield Request(url=url, callback=self.parse, meta={'page':page}, dont_filter=True)

    def parse(self, response):
        '''
        数据处理主方法，通过xpath来抓取每一个元素
        :param response: 网页反应参数
        :return: item实例
        '''
        products = response.xpath("//*[@id='plist']/ul/li")

        for product in products:

            item = JdspiderItem()
            item['title'] = product.xpath(".//div/div[3]/a/em/text()").extract_first().strip()
            # 标题
            item['price'] = product.xpath(".//div/div[2]/strong[1]/i/text()").extract_first()
            # 价格
            item['pic'] = product.xpath(".//div/div[1]/a/img/@src").extract_first()
            # 图片链接
            item['comment'] = product.xpath(".//div/div[4]/strong/a/text()").extract_first()
            # 评论
            item['store'] = product.xpath(".//div/div[5]/span/a/text()").extract_first()
            # 店家
            yield item
