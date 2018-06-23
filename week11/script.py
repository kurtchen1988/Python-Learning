import json
from mitmproxy import ctx

# 响应时自动执行的函数
def response(flow):
    url = 'https://api.m.jd.com/client.action?functionId=search'
    if flow.request.url.startswith(url):
        text = flow.response.text
        data = json.loads(text)
        shoplist = data.get("wareInfo")
        for shop in shoplist:
            item = {
                'spuId':shop.get('spuId'),
                'title':shop.get('wname'),
                'price':shop.get('jdprice'),
                'reviews':shop.get('reviews'),

            }
            ctx.log.info(str(item))