# -*- coding: utf-8 -*-
import scrapy
from dangdang.items import DangdangItem
from scrapy.http import Request

class DdSpider(scrapy.Spider):
    name = 'dd'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://category.dangdang.com/pg1-cid4008154.html']

    def parse(self, response):
        item = DangdangItem()
        item["title"] = response.xpath("//a[@name='itemlist-picture']/@title").extract()
        item["link"] = response.xpath('//a[@name="itemlist-picture"]/@href').extract()
        item["comment"] = response.xpath('//a[@dd_name="单品评论"]/text()').extract()

        yield item #把item传递给pipeline
        for i in range(2,81):
            url='http://category.dangdang.com/pg'+str(i)+'-cid4008154.html'
            yield Request(url,callback=self.parse)