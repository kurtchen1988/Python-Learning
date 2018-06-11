# -*- coding: utf-8 -*-
import scrapy, re
from csdnspider.items import CsdnspiderItem
from scrapy_redis.spiders import RedisSpider

class CsdnSpider(RedisSpider):
    name = 'csdn'
    #allowed_domains = ['edu.csdn.net/courses/k']
    #start_urls = ['http://edu.csdn.net/courses/k/']
    redis_key = 'csdnspider:start_urls'

    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(CsdnSpider, self).__init__(*args, **kwargs)

    def parse(self, response):

        item = CsdnspiderItem()
        item['title'] = response.xpath(".//*[@id='course_detail_block1']/div/div[2]/h1/text()").extract_first().strip()
        item['hours'] = response.xpath(".//*[@id='course_detail_block1']/div/div[2]/div[1]/span[2]/text()").extract_first()
        item['teacher'] = response.xpath(".//div[@class='professor_name']/a/text()").extract_first()
        item['people'] = response.xpath(".//*[@id='course_detail_block1']/div/div[2]/div[2]/span[2]/text()").extract_first()
        item['number'] = response.xpath(".//*[@id='course_detail_block1']/div/div[2]/div[2]/span[3]/span[2]/text()").extract_first()
        item['price'] = response.xpath(".//div[@class='sale']/span[@class='money']/text()").extract_first().strip()
        item['desciption'] = response.xpath(".//div[@class='outline_discribe_box J_outline_discribe_box']/span/text()").extract_first().strip()

        print(item)
        yield item

