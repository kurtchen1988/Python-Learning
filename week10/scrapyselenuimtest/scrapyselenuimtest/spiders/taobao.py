# -*- coding: utf-8 -*-
from scrapy import Request, Spider
from urllib.parse import quote
from scrapyselenuimtest.items import ProductItem

#D:\Python\练习\week10\scrapyselenuimtest\scrapyselenuimtest\items.py

class TaobaoSpider(Spider):
    name = 'taobao'
    allowed_domains = ['www.taobao.com']
    base_url = ['http://s.taobao.com/search?q=']

    def start_requests(self):
        for keyword in self.settings.get('KEYWORDS'):
            for page in range(1, self.settings.get('MAX_PAGE')+1):
                url = self.base_url + quote(keyword)
                yield Request(url=url, callback=self.parse, meta={'page':page}, dont_filter = True)

    def parse(self, response):
        products = response.xpath('//div[@id="mainsrp-itemlist"]//div[@class="items"][1]//div[contains(@class,"item")]')
        for product in products:
            item = ProductItem()
            item['price'] = ''.join(products.xpath('.//div[contains(@class,"price")]//text()').extract()).strip()
            item['title'] = ''.join(products.xpath('.//div[contains(@class,"title")]//text()').extract()).strip()
            item['shop'] = ''.join(products.xpath('.//div[contains(@class,"shop")]//text()').extract()).strip()

            item['image'] = ''.join(products.xpath('.//div[@class="pic"]//img[contains(@class,"img")]/@data-src').extract()).strip()
            item['deal'] = ''.join(products.xpath('.//div[contains(@class,"deal-cnt")]//text()').extract()).strip()
            item['location'] = ''.join(products.xpath('.//div[contains(@class,"location")]//text()').extract()).strip()

            yield item
