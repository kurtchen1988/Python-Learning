import requests
import json


def fanyi(keyword):
    url = "http://fanyi.baidu.com/sug"

    data = {'kw':keyword}


    headers = {'Content-Length':len(data)}


    res = requests.post(url, data=data)

    str_json = res.content.decode("utf-8")
    #print(str_json)
    myjson = json.loads(str_json)

    print(myjson['data'][0]['v'])


if __name__ == '__main__':
    while True:
        keyword = input("请输入要翻译词：")
        if keyword == 'q':
            break
        fanyi(keyword)