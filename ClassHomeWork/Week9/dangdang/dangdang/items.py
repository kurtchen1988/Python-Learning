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
    name = scrapy.Field() # 书名
    price = scrapy.Field() # 价格
    pic = scrapy.Field() # 图片URL
    author = scrapy.Field() # 作者
    publisher = scrapy.Field() # 出版商
    comments = scrapy.Field() # 评论数量
    pubdate = scrapy.Field() # 发行日期
    description = scrapy.Field()  # 描述

