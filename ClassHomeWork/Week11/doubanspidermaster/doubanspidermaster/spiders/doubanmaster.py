# -*- coding: utf-8 -*-
import scrapy


class DoubanmasterSpider(scrapy.Spider):
    name = 'doubanmaster'
    allowed_domains = ['book.douban.com']
    start_urls = ['http://book.douban.com/']

    def parse(self, response):
        pass
