# -*- coding: utf-8 -*-
import scrapy, re
from doubanspider.items import DoubanspiderItem
from scrapy_redis.spiders import RedisSpider

class DoubanSpider(RedisSpider):
    name = 'douban'
    #allowed_domains = ['book.douban.com']
    #start_urls = ['http://book.douban.com/']
    redis_key = 'doubanspider:start_urls'

    def __init__(self, *args, **kwargs):
        domain = kwargs.pop('domain','')
        self.allowed_domains = filter(None, domain.split(','))
        super(DoubanSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        item = DoubanspiderItem()

        if response.xpath('/html/head/meta[@http-equiv="mobile-agent"]/@content').re('url=https:\/\/m.douban.com\/book\/subject\/(.*?)\/'):
            item['BookID'] = response.xpath('/html/head/meta[@http-equiv="mobile-agent"]/@content').re('url=https:\/\/m.douban.com\/book\/subject\/(.*?)\/')[0] # 书ID
        else:
            item['BookID'] = ''

        item['BookName'] = response.xpath('//*[@id="wrapper"]/h1/span/text()').extract_first() # 书名

        if response.xpath('//*[@id="info"]/a[1]/text()').extract_first():
            item['Author'] = response.xpath('//*[@id="info"]/a[1]/text()').extract_first()
        elif response.xpath('//*[@id="info"]').re('作者:<\/span> (.*?)<br'):
            item['Author'] = response.xpath('//*[@id="info"]').re('作者:<\/span> (.*?)<br')[0] # 作者
        else:
            item['Author'] = ''

        if response.xpath('//div[@id="info"]').re('出版社:<\/span> (.*?)<br'):
            item['Publisher'] = response.xpath('//div[@id="info"]').re('出版社:<\/span> (.*?)<br')[0]
        else:
            item['Publisher'] = ''

        if response.xpath('//div[@id="info"]').re('原作名:<\/span> (.*?)<br'):
            item['OriginName'] = response.xpath('//div[@id="info"]').re('原作名:<\/span> (.*?)<br')[0]
        else:
            item['OriginName'] = ''

        if response.xpath('//*[@id="info"]/span[4]/a/text()').extract_first():
            item['Translatoer'] = response.xpath('//*[@id="info"]/span[4]/a/text()').extract_first()
        elif response.xpath('//div[@id="info"]').re('译者:<\/span> (.*?)<br'):
            item['Translatoer'] = response.xpath('//div[@id="info"]').re('译者:<\/span> (.*?)<br')[0] # 译者
        else:
            item['Translatoer'] = ''

        if response.xpath('//div[@id="info"]').re('出版年:<\/span> (.*?)<br'):
            item['YearPublish'] = response.xpath('//div[@id="info"]').re('出版年:<\/span> (.*?)<br')[0]
        else:
            item['YearPublish'] = ''

        if response.xpath('//div[@id="info"]').re('页数:<\/span> (.*?)<br'):
            item['PageNumber'] = response.xpath('//div[@id="info"]').re('页数:<\/span> (.*?)<br')[0]
        else:
            item['PageNumber'] = ''

        if response.xpath('//div[@id="info"]').re('定价:<\/span> (.*?)<br'):
            item['Price'] = response.xpath('//div[@id="info"]').re('定价:<\/span> (.*?)<br')[0]
        else:
            item['Price'] = ''

        if response.xpath('//div[@id="info"]').re('装帧:<\/span> (.*?)<br'):
            item['Binding'] = response.xpath('//div[@id="info"]').re('装帧:<\/span> (.*?)<br')[0]
        else:
            item['Binding'] = ''

        if response.xpath('//*[@id="info"]/a[2]/text()').extract_first():
            item['Collection'] = response.xpath('//*[@id="info"]/a[2]/text()').extract_first()
        elif response.xpath('//div[@id="info"]').re('丛书:<\/span> (.*?)<br'):
            item['Collection'] = response.xpath('//div[@id="info"]').re('丛书:<\/span> (.*?)<br')[0]
        else:
            item['Collection'] = ''

        if response.xpath('//div[@id="info"]').re('ISBN:<\/span> (.*?)<br'):
            item['ISBN'] = response.xpath('//div[@id="info"]').re('ISBN:<\/span> (.*?)<br')[0]
        else:
            item['ISBN'] = ''

        item['Rates'] = response.xpath('//*[@id="interest_sectl"]/div/div[2]/strong/text()').extract_first() # 评分
        item['CommentNum'] = response.xpath('//*[@id="interest_sectl"]/div/div[2]/div/div[2]/span/a/span/text()').extract_first() # 评论数


        print(item)
        yield item