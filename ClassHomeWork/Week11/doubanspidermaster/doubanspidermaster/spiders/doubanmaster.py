# -*- coding: utf-8 -*-
import scrapy, requests, re
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from doubanspidermaster.items import DoubanspidermasterItem
from scrapy import Request


class DoubanmasterSpider(scrapy.Spider):
    name = 'doubanmaster'
    allowed_domains = ['book.douban.com']
    start_urls = ['https://book.douban.com/tag/?view=type&icn=index-sorttags-all']
    base_urls = 'https://book.douban.com/subject/25862578/'
    progress_urls= 'https://book.douban.com/tag/'

    rules = (
        Rule(LinkExtractor(allow=('https://book.douban.com/subject/[0-9]+/',)), callback='parse_item',
             follow=True),
    )

    def start_requests(self):
        '''
        爬虫开始方法，将类别页面传递给parse
        :return: None
        '''
        yield Request(url=self.start_urls[0], callback=self.parse, dont_filter=True)

    def parse(self, response):
        '''
        将每一类型的书列表页面传递给parse_item,默认传递50页。在settings中的MAX_PAGE字段设置页数
        :param response: 网页返回参数
        :return: yield item
        '''
        tags = response.xpath('.//table[@class="tagCol"]/tbody/tr/td/a/text()').extract()

        for tag in tags:
            for page in range(0,self.settings.get("MAX_PAGE")):
                urls = self.progress_urls + tag + '?start=' + str(page * 20)
                print(urls)
                yield Request(url=self.progress_urls+tag+'?start='+str(page*20), callback=self.parse_item, dont_filter=True)




    def parse_item(self, response):
        '''
        对书的类型爬取操作，然后，将爬取各种类型的书的url写入redis数据库
        :param response:
        :return:
        '''
        item = DoubanspidermasterItem()
        book_urls = response.xpath('//div[@class="pic"]/a[@class="nbg"]/@href').extract()

        for book in book_urls:
            item['url'] = book
            print(item)
            yield item