# -*- coding: utf-8 -*-
import scrapy
import time
import json
import execjs
import os
from PIL import Image
import base64
from scrapy.http.cookies import CookieJar

class ZhihuspiderSpider(scrapy.Spider):
    name = 'zhihuSpider'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']
    name = 'login'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']
    login_url = 'https://www.zhihu.com/api/v3/oauth/sign_in'  # 登陆的url
    captcha_url = 'https://www.zhihu.com/api/v3/oauth/captcha?lang=en'# 验证码地址
    inbox_url = 'https://www.zhihu.com/inbox'#测试链接
    logincookie = None

    # 登陆时，需要的信息
    user = ''
    password = ''
    client_id = 'c3cef7c66a1843f8b3a9e6a1e3160e20'

    login_headers = {
        'authorization': 'oauth ' + client_id,
        'Host': 'www.zhihu.com',
        'Origin': 'https://www.zhihu.com',
        'Referer': 'https://www.zhihu.com/signup?next=%2F',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36 QQBrowser/4.3.4986.400',
        'X-UDID': 'ADAg-7cpUg2PTtLig29RVbKuOrt_QwlJn_8=',
        'X-Xsrftoken': '7cc9ff84-ca8d-491d-9f6e-b4733fdae31c',
        'If-None-Match': '7eb4ebdc523b46e04c7fa978993f57f559d7ed8b'
    }


    custom_settings = {
        "COOKIES_ENABLED": True,
        "DOWNLOAD_DELAY": 0.5,
    }

    def parse(self, response):
        '''登陆验证结束，正式开始处理爬虫'''
        if response.status == 200:
            print('登录成功，可以开始爬取')
        else:
            print(response.text)


    def get_timestamp(self):
        '''时间戳生成函数'''
        timestamp = int(time.time() * 1000)
        return str(timestamp)

    def get_signature(self):
        '''通过网页上的js生成签名'''
        path = os.path.dirname(os.path.abspath(__file__))
        fp=open(path+'/zhihu.js')
        js=fp.read()
        fp.close()
        ctx=execjs.compile(js)
        signature=ctx.call('getSignature',self.get_timestamp())
        return signature

    def start_requests(self):
        '''开始爬取登录页面'''
        yield scrapy.Request('https://www.zhihu.com/api/v3/oauth/captcha?lang=en',headers=self.login_headers,
                             callback=self.ifCaptcha,dont_filter=True)

    def ifCaptcha(self,response):
        captcha_info = json.loads(response.text)
        params={
            'client_id':self.client_id,
            'grant_type':'password',
            'timestamp':self.get_timestamp(),
            'source':'com.zhihu.web',
            'signature':self.get_signature(),
            'username':self.user,
            'password':self.password,
            'captcha':'',
            'lang':'cn',
            'ref_source':'homepage',
            'utm_source':'',
        }
        if 'show_captcha' in captcha_info:
            if captcha_info['show_captcha']:
                 print('出现验证码')
                 yield scrapy.Request(url=self.captcha_url, headers=self.login_headers, method='PUT', callback=self.captcha_process, meta=params)
            else:
                print('无验证码')
                yield scrapy.FormRequest(url=self.login_url, headers=self.login_headers, formdata=params, method='POST', callback=self.check_login)
        else:
            self.logger.warning('出现未知异常： %s', response.text)




    def captcha_process(self,response):
        '''处理验证码'''
        #第一步： 获取验证码(把base64图片数据流解码，生成图片)
        print(response.text)
        res_dit = json.loads(response.text)
        img_base64=res_dit['img_base64']
        pictureData = base64.b64decode(img_base64)
        with open("captcha.gif", "wb") as f:
            f.write(pictureData)
            f.close()
        try:
            img=Image.open('captcha.gif')
            img.show()
        except:
            print('转图片失效')

        #检查验证码是否写的正确
        captcha = input("输入验证码")
        params_checkCaptcha={
            'input_text':captcha
        }
        yield scrapy.FormRequest(url=self.captcha_url, headers=self.login_headers, formdata=params_checkCaptcha, method='POST',
                                 meta=params_checkCaptcha, callback=self.check_captcha)



    def check_captcha(self,response):
        '''检查验证码是否正确'''
        res_dit=json.loads(response.text)

        params={
            'client_id':self.client_id,
            'grant_type':'password',
            'timestamp':self.get_timestamp(),
            'source':'com.zhihu.web',
            'signature':self.get_signature(),
            'username':self.user,
            'password':self.password,
            'captcha':'',
            'lang':'cn',
            'ref_source':'homepage',
            'utm_source':'',
        }
        params['captcha']=response.meta['input_text']

        if 'success' in res_dit:
            print('验证码正确')
            yield scrapy.FormRequest(url=self.login_url, headers=self.login_headers, formdata=params, method='POST',
                                    callback=self.check_login)
        else:
            print(response.text)


    def check_login(self,response):
        '''登陆结果判断 如果成功就把cookie存文件夹里'''
        response_dit=json.loads(response.text)

        if 'user_id' in response_dit:
            print('登陆成功')
            self.get_cookies(response)
            yield scrapy.Request(url=self.inbox_url, headers=self.login_headers, callback=self.parse,meta=self.logincookie)
        else:
            print('登陆异常 ： '+response.text)


    def get_cookies(self,res):
        '''获取登陆成功后的cookies 写入文件夹以便之后使用'''
        cookie_jar = CookieJar()
        self.logincookie=cookie_jar
        cookie_jar.extract_cookies(res, res.request)
        with open('cookies.txt', 'w') as f:
            for cookie in cookie_jar:
                f.write(str(cookie) + '\n')

    def get_header(self, refer):
        '''处理所有request的头信息'''
        request_headers = {
            "Accept": "application/json, text/plain, */*",
            # "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "authorization": "oauth c3cef7c66a1843f8b3a9e6a1e3160e20",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": '__DAYU_PP=mIAzqR6JjZJIV3AmU62v2ae19319dc81; q_c1=2f36189ed07842fea5d63abcf6dcfe6c|1521378566000|1521378566000; capsion_ticket="2|1:0|10:1521554442|14:capsion_ticket|44:M2IyYzBlYjY2NWI4NGQ0Y2I3NmZmMzZkYzhkMTgxZTk=|6923e50d6edf43e519899682e589376d813babd22d76629d016fb6db32874305"; _zap=34f289cd-73fc-4362-a6fa-5c39b0c71f35; r_cap_id="ZDc5ZmZlZGY4MDgwNGZjMzhkYzM3MTJiZTc0MmQ5ZDg=|1521561292|eee96888d4bc168d30324208e0b00a96d750374e"; cap_id="NjM1MWJlY2QwMGY5NGJlMGE1NjVjYTZhNzNhMjNmNjA=|1521561292|a076be34c57e4a383bbb0f177db96b3224cecfd8"; __utma=51854390.1141490050.1521384369.1521556000.1521556000.6; __utmz=51854390.1521384369.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/topics; l_cap_id="MmZhMzdhYTRkYzRhNDZmMGEzZDg2YzgyM2VkZmUyMDM=|1521561292|3a4e77d02b1e1031f6dac87af28b464ecc5ce90d"; d_c0="AEBr7njMTw2PTg-BnKIjeG7KuLINqK1ENFo=|1521473500"; _xsrf=b346d3a1d11d099f8a5fd07b9b77b2d8; __utmc=51854390; __utmv=51854390.000--|2=registration_date=20180318=1^3=entry_date=20180320=1',
            "Host": "www.zhihu.com",
            "Referer": str(refer),
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.3",
            "x-udid": "APBvzZ6uUw2PTunjl2NE4hNTFng78JkWYGo="
        }
        return request_headers

    def post_content(self, url, header, param):
        pass