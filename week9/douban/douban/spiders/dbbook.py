# -*- coding: utf-8 -*-
import scrapy


class DbbookSpider(scrapy.Spider):
    name = 'dbbook'
    allowed_domains = ['book.douban.com']
    start_urls = ['http://book.douban.com/top250?start=0']

    def parse(self, response):
        print("helloIAMSPIDER")
