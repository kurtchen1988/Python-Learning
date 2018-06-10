from scrapy.spider import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from csdnspidermaster.items import CsdnMasterItem


class CsdnSpider(CrawlSpider):
    name = 'csdnmaster'
    #allowed_domains = ['edu.csdn.net/courses/k']
    start_urls = ['http://edu.csdn.net/courses/k']
    redis_key = 'csdnspider:start_urls'

    rules = (
        Rule(LinkExtractor(allow=('http://edu.csdn.net/courses/k/p[0-9]+/',)), callback='parse_item',
             follow=True),
    )

    def parse(self, response):

        item = CsdnMasterItem()
        itemlist = response.xpath(".//div[@class='course_dl_list']")
        for items in itemlist:
            item['url'] = items.xpath(".//a/@href").extract_first()
            print(item)
            yield item