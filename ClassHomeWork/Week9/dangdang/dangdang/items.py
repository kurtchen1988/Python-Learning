# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DangdangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    '''Item类，包含所有要爬取的信息
    '''
    name = scrapy.Field()
    price = scrapy.Field()
    pic = scrapy.Field()
    publisher = scrapy.Field()
    comments = scrapy.Field()
    pubdate = scrapy.Field()
    description = scrapy.Field()

