import random, requests

proxy_list = [
    '182.39.6.245:38634',
    '115.210.181.31:34301',
    '123.161.152.38:23201',
    '222.85.5.187:26675',
    '123.161.152.31:23127',
]

proxy = random.choice(proxy_list)
print(proxy)
proxies = {
    'http':'http://'+proxy,
    'https':'https://'+proxy,
}
try:
    response = requests.get('http://httpbin.org/get', proxies=proxies)
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print('Error', e.args)