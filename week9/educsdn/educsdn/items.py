# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CoursesItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    url = scrapy.Field()
    pic = scrapy.Field()
    teacher = scrapy.Field()
    time = scrapy.Field()
    price = scrapy.Field()
    pass
