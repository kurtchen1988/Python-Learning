# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
import scrapy
from scrapy.item import Item, Field
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join


class CsdnspiderItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    hours = scrapy.Field()
    teacher = scrapy.Field()
    people = scrapy.Field()
    number = scrapy.Field()
    price = scrapy.Field()
    desciption = scrapy.Field()

class CsdnLoader(ItemLoader):
    default_item_class = CsdnspiderItem
    default_input_processor = MapCompose(lambda s: s.strip())
    default_output_processor = TakeFirst()
    description_out = Join()
