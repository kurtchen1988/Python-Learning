# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request, FormRequest

class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['iqianyue.com']
    start_urls = ['http://iqianyue.com/']
    header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"}

    def start_requests(self):
    #如果没有这个方法的话，会默认使用start_urls里面的网址。有了这个之后就会取代。
        #首先爬一次登录页，然后进入回调函数parse()
        return [Request("http://edu.iqianyue.com/index_user_login.html", meta={"cookiejar":1}, callback=self.parse)]
        #先爬一遍看到的html网页，然后把meta信息的cookiejar设置为1，就是我们看到的状态。callback这个就是回调函数，也就是
        #设置爬到之后谁来处理信息。过程就是首先进行Request函数，再去给回调函数处理其数据。

    def parse(self, response):
        # 设置要传递的post信息，此时没有验证码字段
        data ={
            "number":"kurtbantu",
            "passwd":"chenchen1988"
        }
        #key是字段名，value是字段值

        print("登陆中")
        # 通过FormRequest.from_response()进行登录
        return [FormRequest.from_response(response,
                                          #设置coockie信息
                                          meta={"cookiejar": response.meta["cookiejar"]},
                                          #设置headers信息模拟成浏览器
                                          headers=self.header,
                                          #设置post表单中的数据
                                          formdata=data,
                                          #设置回调函数，此时回调函数为next()
                                          callback=self.next,)]
    def next(self, response):
        #a=response.body
        # 这里可以直接用response.body来提取响应的信息，然后赋给a,这样就可以处理
        data=response.body
        fh=open("D:\\Python\\练习\\iofile\\a.html","wb")
        fh.write(data)
        fh.close()
        #用response.body读取，并且写入对应的文件里
        print(response.xpath("/html/head/title/text()").extract())
        yield Request("http://edu.iqianyue.com/index_user_index", callback=self.next2, meta={"cookiejar": True})
        #这里写的是你希望访问的网址，登录后.这里返回个人中心。这里通过这么写，让其保持登录的状态。这里的response是登陆
        #成功后的界面

    def next2(self, response):
        data=response.body
        fh = open("D:\\Python\\练习\\iofile\\b.html", "wb")
        fh.write(data)
        fh.close()
        print(response.xpath("/html/head/title/text()").extract())
        #这里的response才是我们个人中心页面