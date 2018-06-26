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
        爬虫开始方法，通过对页数参数读取，创造一个for循环，再通过yield来创建一个Request并访问parse方法
        :return: yield item
        '''
        yield Request(url=self.start_urls[0], callback=self.parse, dont_filter=True)

    def parse(self, response):
        '''
        对具体爬取数据的操作
        :param response: 网页返回参数
        :return: yield item
        '''
        tags = response.xpath('.//table[@class="tagCol"]/tbody/tr/td/a/text()').extract()
        '''
        for tag in tags:
            for page in range(0,self.settings.get("MAX_PAGE")):
                urls = self.progress_urls + tag + '?start=' + str(page * 20)
                print(urls)
                yield Request(url=self.progress_urls+tag+'?start='+str(page*20), callback=self.parse_item, dont_filter=True)
        '''

        for page in range(0,self.settings.get("MAX_PAGE")):
            urls = self.progress_urls + tags[0] + '?start=' + str(page * 20)
            print(urls)
            yield Request(url=self.progress_urls+tags[0]+'?start='+str(page*20), callback=self.parse_item, dont_filter=True)


    def parse_item(self, response):
        item = DoubanspidermasterItem()
        book_urls = response.xpath('//li[@class="pic"]/a[@class="nbg"]/@href').extract()
        for book in book_urls:
            item['url'] = book
            print(item)
            yield item