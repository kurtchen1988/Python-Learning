# -*- coding: utf-8 -*-
import scrapy, re
from csdnspidermaster.items import CsdnMasterItem
from scrapy_redis.spiders import RedisSpider

class CsdnSpider(RedisSpider):
    name = 'csdnmaster'
    #allowed_domains = ['edu.csdn.net/courses/k']
    #start_urls = ['http://edu.csdn.net/courses/k/']
    redis_key = 'csdnspider:start_urls'

    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(CsdnSpider, self).__init__(*args, **kwargs)

    def parse(self, response):

        item = CsdnMasterItem()
        item['url'] = response.xpath(".//*[@id='course_detail_block1']/div/div[2]/h1/text()").extract_first().strip()

        print(item)
        return item

