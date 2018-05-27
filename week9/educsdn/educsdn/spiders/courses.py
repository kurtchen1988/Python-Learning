# -*- coding: utf-8 -*-
import scrapy
from educsdn.items import  CoursesItem

class CoursesSpider(scrapy.Spider):
    name = 'courses'
    allowed_domains = ['edu.csdn.net']
    start_urls = ['http://edu.csdn.net/courses/o280/p1']
    p=1
    def parse(self, response):
        dlist = response.selector.css("div.course_dl_list")
        for dd in dlist:
            item = CoursesItem()
            item['title'] = dd.css("span.title::text").extract_first()
            item['url'] = dd.css("a::attr(href)").extract_first()
            item['pic'] = dd.css("img::attr(src)").extract_first()
            item['teacher'] = dd.re_first("<p>讲师：(.*?)</p>")
            item['time'] = dd.re_first("<em>([0-9]+)</em>课时")
            item['price'] = dd.re_first("￥([0-9\.]+)")
            print(item)
            yield item
        self.p += 1
        if self.p <4:
            next_url = 'http://edu.csdn.net/courses/o280/p'+str(self.p)
            url = response.urljoin(next_url)
            yield scrapy.Request(url=url, callback=self.parse)