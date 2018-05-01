import requests
import re, time


s =requests.Session()

def doLogin():
    login_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2018421832726'

    data = {'email': '13520319616',
            'icode':'',
            'origURL': 'http://www.renren.com/home',
            'domain': 'renren.com',
            'key_id': '1',
            'captcha_type': 'web_login',
            'password': '2a5222468d922a8d3eaaa43a6f8d5d1cb34e196ba50c9147fe8935fe020ab6f9',
            'rkey': '06142e54e56046eb7e7906cf70cac027',
            'f': 'http%3A%2F%2Fwww.renren.com%2F965541786',}

    res = s.post(login_url, data=data)
    print("login Successfully")

def myHome():
    url = 'http://www.renren.com/965541786'
    res = s.get(url)

    html = res.content.decode('utf-8')
    # html = gzip.decompress(res.read()).decode('utf-8')

    # print(html)
    print(re.findall("<title>(.*?)</title>", html))


if __name__ == "__main__":
    print("登录中。。。")
    doLogin()
    time.sleep(2)
    myHome()