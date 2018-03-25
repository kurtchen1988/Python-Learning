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

    headers = {
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
        yield scrapy.Request('https://www.zhihu.com/api/v3/oauth/captcha?lang=en',headers=self.headers,
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
                 yield scrapy.Request(url=self.captcha_url, headers=self.headers, method='PUT', callback=self.captcha_process, meta=params)
            else:
                print('无验证码')
                yield scrapy.FormRequest(url=self.login_url, headers=self.headers, formdata=params, method='POST', callback=self.check_login)
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
        yield scrapy.FormRequest(url=self.captcha_url, headers=self.headers, formdata=params_checkCaptcha, method='POST',
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
            yield scrapy.FormRequest(url=self.login_url, headers=self.headers, formdata=params, method='POST',
                                    callback=self.check_login)
        else:
            print(response.text)


    def check_login(self,response):
        '''登陆结果判断 如果成功就把cookie存文件夹里'''
        response_dit=json.loads(response.text)

        if 'user_id' in response_dit:
            print('登陆成功')
            self.get_cookies(response)
            yield scrapy.Request(url=self.inbox_url, headers=self.headers, callback=self.parse,meta=self.logincookie)
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
