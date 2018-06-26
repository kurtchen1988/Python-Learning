# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanspiderItem(scrapy.Item):
    # define the fields for your item here like:
    BookID = scrapy.Field()
    BookName = scrapy.Field()
    Author = scrapy.Field()
    Publisher = scrapy.Field()
    OriginName = scrapy.Field()
    Translatoer = scrapy.Field()
    YearPublish = scrapy.Field()
    PageNumber= scrapy.Field()
    Price = scrapy.Field()
    Binding = scrapy.Field()
    Collection = scrapy.Field()
    ISBN = scrapy.Field()
    Rates = scrapy.Field()
    CommentNum = scrapy.Field()
    pass
