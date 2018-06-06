# -*- coding: utf-8 -*-
import scrapy


class HbSpider(scrapy.Spider):
    name = 'hb'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/get']

    def parse(self, response):
        print(response.body)
