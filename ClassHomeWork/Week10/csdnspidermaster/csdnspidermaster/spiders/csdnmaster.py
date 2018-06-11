from scrapy.spider import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from csdnspidermaster.items import CsdnMasterItem
from scrapy import Request

class CsdnSpider(CrawlSpider):
    name = 'csdnmaster'
    #allowed_domains = ['edu.csdn.net/courses/k']
    start_urls = ['http://edu.csdn.net/courses/k/p']
    base_url = 'http://edu.csdn.net/courses/k/p'
    #redis_key = 'csdnspider:start_urls'

    rules = (
        Rule(LinkExtractor(allow=('http://edu.csdn.net/courses/k/p[0-9]+/',)), callback='parse_item',
             follow=True),
    )

    def start_requests(self):
        '''
        爬虫开始方法，通过对页数参数读取，创造一个for循环，再通过yield来创建一个Request并访问parse方法
        :return: yield item
        '''
        for page in range(1, self.settings.get('MAX_PAGE')+1):
            url = self.base_url+str(page)
            yield Request(url=url, callback=self.parse, dont_filter=True)

    def parse(self, response):
        '''
        对具体爬取数据的操作
        :param response: 网页返回参数
        :return: yield item
        '''
        item = CsdnMasterItem()
        itemlist = response.xpath(".//div[@class='course_dl_list']")
        for items in itemlist:
            item['url'] = items.xpath(".//a/@href").extract_first()
            yield item