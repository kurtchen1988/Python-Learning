from urllib import request,parse
import re, time
from http import cookiejar

cookie = cookiejar.CookieJar()
cookie_handler = request.HTTPCookieProcessor(cookie)

opener = request.build_opener(cookie_handler)

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

    data = parse.urlencode(data)

    headers = {
        'Content-Length':len(data)
    }

    req = request.Request(login_url, data=bytes(data, encoding='utf-8'), headers=headers)
    res = opener.open(req)
    print("login Successfully")

def myHome():
    login_url = 'http://www.renren.com/965541786'
    req = request.Request(login_url)
    res = opener.open(req)

    html = res.read().decode('utf-8')
    # html = gzip.decompress(res.read()).decode('utf-8')

    # print(html)
    print(re.findall("<title>(.*?)</title>", html))


if __name__ == "__main__":
    print("登录中。。。")
    doLogin()
    time.sleep(2)
    myHome()