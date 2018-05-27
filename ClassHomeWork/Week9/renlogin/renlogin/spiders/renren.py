# -*- coding: utf-8 -*-
import scrapy,json


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['www.renren.com']
    start_urls = ['http://www.renren.com/']

    def start_requests(self):
        '''
        爬虫开始调用方法。此方法用yield与scrapy的FormRequest把账户与相关信息提交。并使用
        回调方法访问parse来接下来处理返回的代码。请注意这里的用户名与密码是老师给的，已经
        失效。请测试者自行输入有效的用户名与密码。
        :return: None
        '''
        login_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2018421832726'
        # 登录页面的URL
        data = {'email': '13520319616',
                'icode': '',
                'origURL': 'http://www.renren.com/home',
                'domain': 'renren.com',
                'key_id': '1',
                'captcha_type': 'web_login',
                'password': '2a5222468d922a8d3eaaa43a6f8d5d1cb34e196ba50c9147fe8935fe020ab6f9',
                'rkey': '06142e54e56046eb7e7906cf70cac027',
                'f': 'http%3A%2F%2Fwww.renren.com%2F965541786', }
        # 登录的表单信息，其中用户名与密码请自行输入正确值
        yield scrapy.FormRequest(
            url = login_url,
            formdata = data,
            callback = self.parse
        )

    def parse(self, response):
        '''
        爬虫程序经过start_requests方法后调用此方法。通过对response代码的json包装，取出
        其中对应failDescription键的字段。如果这个字段存在，证明登录失败，并且这个字段是
        描述登录失败的原因，打印登录失败与原因。如果这个字段不存在，说明登录成功打印登录成功。
        :param response:
        :return:
        '''
        res = json.loads(response.text)
        if(res['failDescription']):
            print("登录失败，原因是："+res['failDescription'])
        else:
            print("登录成功")
