# -*- coding: utf-8 -*-
import scrapy


class WenkuSpider(scrapy.Spider):
    name = 'wenku'
    allowed_domains = ['wenku.baidu.com']
    start_urls = ['https://wenku.baidu.com/search?word=python&pn=0', 'https://wenku.baidu.com/search?word=python&pn=10', 'https://wenku.baidu.com/search?word=python&pn=20']
    p=0
    def parse(self, response):
        #print("hello scrapy")
        dllist = response.selector.xpath("//dl")

        for dd in dllist:
            print(dd.css("p.fl a::attr('title')").extract_first())
        print("="*70)
        self.p += 1
        if self.p < 10:
            next_url = 'https://wenku.baidu.com/search?word=python&pn='+str(self.p*10)
            url = response.urljoin(next_url)
            yield scrapy.Request(url=url, callback=self.parse)