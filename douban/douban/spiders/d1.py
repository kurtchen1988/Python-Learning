# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request, FormRequest
import urllib.request
import os

class D1Spider(scrapy.Spider):
    name = 'd1'
    allowed_domains = ['douban.com']
    #start_urls = ['http://douban.com/']
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"}

    def start_requests(self):
        #第一次请求页面，可以将post直接爬取，或者先爬一遍页面，这样就可以判断是否有验证码
        return [Request("https://accounts.douban.com/login", meta={"cookiejar": 1}, callback=self.parse)]

    def parse(self, response):
        # 判断是否有验证码
        captcha=response.xpath("//img[@id='captcha_image']/@src").extract()
        if len(captcha)>0:
            print("此时有验证码")
            #将验证码存储到本地
            localpath="D:\\Python\\yzm\\captcha.png"
            urllib.request.urlretrieve(captcha[0], filename=localpath)
            # 将验证码的图片存储到本地。使用urllib的urlretrieve这个方法
            #captcha_value = input("请到D:\Python\练习\douban\yzm\查看captcha.png验证码")
            cmd="D:/Python35/python.exe D:/Python35/yzm/YDMPythonDemo.py"
            r=os.popen(cmd)
            captcha_value=r.read()
            print("当前验证码自动识别结果为"+captcha_value)
            data = {
                "captcha-solution":captcha_value,
                "redir": "https://www.douban.com/people/122581561/",
                "form_email": "15868146400",
                "form_password": "lifeIsGreat1!"
            }
        else:
            data = {
                "redir": "https://www.douban.com/people/122581561/",
                "form_email": "15868146400",
                "form_password":"lifeIsGreat1!"
            }
            #有没有验证码，就是这个data的设置是否一样
        # key是字段名，value是字段值

        print("登陆中")
        # 通过FormRequest.from_response()进行登录
        return [FormRequest.from_response(response,
                                          # 设置coockie信息
                                          meta={"cookiejar": response.meta["cookiejar"]},
                                          # 设置headers信息模拟成浏览器
                                          headers=self.header,
                                          # 设置post表单中的数据
                                          formdata=data,
                                          # 设置回调函数，此时回调函数为next()
                                          callback=self.next, )]

    def next(self, response):
        title=response.xpath("/html/head/title/text()").extract()
        print(title)