# -*- coding: utf-8 -*-
import scrapy, re


class SinaSpider(scrapy.Spider):
    name = 'sina'
    allowed_domains = ['http://news.sina.com.cn']
    start_urls = ['http://news.sina.com.cn/guide/']

    def parse(self, response):
        '''
        页面访问调用方法。首先将页面response代码用xpath把每个大类代码找到，再用xpath
        在这些代码中分别找到第一级标题，第二级标题和第三级标题。将它们遍历并打印
        :param response: 网页反应参数
        :return: None
        '''
        dlist = response.selector.xpath("//div[@class='section']")
        header1 = dlist.xpath(".//h2[@class='tit01']/text()").extract()
        print("第一级标题： ")
        print(header1)
        for d in dlist:
            header2 = d.xpath(".//h3[@class='tit02']/a/text()|.//h3[@class='tit02']/text()").extract()
            print("第二级标题： ")
            print(header2)
        for dd in dlist:
            header3 = dd.xpath(".//ul[@class='list01']/li/a/text()").extract()
            print("第三极标题： ")
            print(header3)