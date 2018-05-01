from urllib import request,parse
import gzip, re

login_url = 'http://www.renren.com/965541786'

headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': 'anonymid=jgnilriow3j5up; depovince=ZJ; _r01_=1; JSESSIONID=abc_aC0fDDX9zfrXumBmw; ick_login=fb938e4e-8c3b-45cd-aab2-e133da8fdfcd; first_login_flag=1; ch_id=10016; wp=1; ln_uact=13520319616; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; jebe_key=459f046f-cae0-49e0-8408-6dcaa8266ffd%7C24a48cb369f8637c5ee2c4a23eb5b93f%7C1525170433105%7C1%7C1525170602293; wp_fold=0; jebecookies=28cbf516-f808-49ac-8db7-583acd0c15e9|||||; _de=8C2F648D7158ED727318288C8F3F21C5; p=a402375854de7766788149979f23d1d26; t=3b4fc2382ff723417881844ba315aa556; societyguester=3b4fc2382ff723417881844ba315aa556; id=965541786; xnsid=e4c19c29; loginfrom=syshome',
        'Host': 'www.renren.com',
        'Referer': 'http://www.renren.com/SysHome.do',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',}

req = request.Request(login_url, headers=headers)
res = request.urlopen(req)

html = res.read().decode('utf-8')
#html = gzip.decompress(res.read()).decode('utf-8')

#print(html)
print(re.findall("<title>(.*?)</title>", html))