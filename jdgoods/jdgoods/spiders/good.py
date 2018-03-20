# -*- coding: utf-8 -*-
import scrapy
import urllib.request
import re
import random
from jdgoods.items import JdgoodsItem
from lxml import etree
from scrapy.http import Request

class GoodSpider(scrapy.Spider):
    name = 'good'
    allowed_domains = ['jd.com']
    start_urls = ['http://jd.com/']

    def start_requests(self):
        ua=["",""]

    def parse(self, response):
        pass
