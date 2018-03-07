# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request, FormRequest
from CSDNSpider.items import CsdnspiderItem
#批改老师请注意，项目编写了items.py, settings.py和pipelines.py。麻烦结合一起查看，谢谢！

class CsdnloginSpider(scrapy.Spider):
    name = 'CSDNLogin'
    allowed_domains = ['csdn.net']
    start_urls = ['http://csdn.net/']
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                            "Chrome/64.0.3282.186 Safari/537.36"}
    #用户代理
    localFile = "D:\\Python\\练习\\CSDNSpider\\CSDNFile\\loginPage.html"
    #存放登录页面的位置
    courseURL = "https://edu.csdn.net/courses/k/p"
    #课程URL页面

    def start_requests(self):
    #先抓一遍，看是否有异常
        return [Request("https://passport.csdn.net/account/login", meta={"cookiejar":1}, callback=self.parse)]

    def parse(self, response):
    #将用户名密码传递给表格进行登录
        loginData={"username":"leejc1212",
                   "password":"chenLing19911212!",
                   }
        print("登录中")
        return [FormRequest.from_response(response, meta={"cookiejar":response.meta["cookiejar"]},headers=self.header,
                formdata=loginData, callback=self.next)]

    def next(self, response):
    #跳转至个人信息网页
        print("跳转至个人信息网页")
        yield Request("https://my.csdn.net/", callback=self.next2, meta={"cookiejar": True})

    def next2(self, response):
    #将个人信息网页保存，并跳转至课程页面
        print("保存个人信息网页")
        data=response.body
        fh=open(self.localFile,"wb")
        fh.write(data)
        fh.close()
        yield Request(self.courseURL+str(1), callback=self.course, meta={"cookiejar": True})

    def course(self, response):
    #通过xpath爬取网页内容
        print("爬取网页内容")
        item = CsdnspiderItem()
        item["courseName"] = response.xpath("//span[@class='title']/text()").extract()
        item["coURL"] = response.xpath("//div[@class='course_dl_list']/a[@target='_blank']/@href").extract()

        yield item
    #传给pipelines

        for i in range(1, 259):
            url = self.courseURL+str(i)
            yield Request(url, callback=self.course)
            #爬取所有259页课程内容

