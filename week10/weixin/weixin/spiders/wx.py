# -*- coding: utf-8 -*-
import scrapy
from weixin.items import WxItem

class WxSpider(scrapy.Spider):
    name = 'wx'
    allowed_domains = ['weixin.sogou.com']
    start_urls = ['http://weixin.sogou.com/weixin?query=python&type=2&page=1&ie=utf8']

    def parse(self, response):
        #解析出当前页面中的所有文章信息
        ullist = response.selector.css("ul.news-list li")
        #遍历文章信息
        for ul in ullist:
            #解析具体信息并封装到item中
            item = WxItem()
            item['title'] = ul.css("h3 a").re_first("<a.*?>(.*?)</a>")
            item['content'] = ul.css("p.txt-info::text").extract_first()
            item['nickname'] = ul.css("a.account::text").extract_first()
            item['date'] = ul.re_first("document.write\(timeConvert\('([0-9]+)'\)\)")
            item['url'] = ul.css("h3 a::attr(href)").extract_first()
            print(item)
            # 交给pipelines（item管道）处理
            yield item

        #解析出下一頁的url地址
        next_url = response.selector.css("#sogou_next::attr(href)").extract_first()
        #判断是否存在
        if next_url:
            url = response.urljoin(next_url) #构建绝对url地址
            yield scrapy.Request(url=url,callback=self.parse) #交给调度去继续爬取下一页信息