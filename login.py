# -*- coding: utf-8 -*-
import scrapy


class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['iqianyue.com']
    start_urls = ['http://iqianyue.com/']

    def parse(self, response):
        pass
