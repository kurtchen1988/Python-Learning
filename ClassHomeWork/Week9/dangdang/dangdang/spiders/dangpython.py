# -*- coding: utf-8 -*-
import scrapy
from dangdang.items import DangdangItem

class DangpythonSpider(scrapy.Spider):
    name = 'dangpython'
    allowed_domains = ['search.dangdang.com']
    start_urls = ['http://search.dangdang.com/?key=python&act=input']

    def parse(self, response):
        '''

        :param response:
        :return:
        '''

        '''
        name = scrapy.Field()
        price = scrapy.Field()
        pic = scrapy.Field()
        publisher = scrapy.Field()
        comments = scrapy.Field()
        pubdate = scrapy.Field()
        description = scrapy.Field()
        '''