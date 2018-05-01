from urllib import request, error

url = "http://www.sfgsdg.com"
req = request.Request(url)
try:
    res = request.urlopen(req)
    html = res.read().decode("utf-8")

    print(len(html))
except Exception as e:
    if hasattr(e,"code"):
        print("HTTPError")
        print(e.reason)
        print(e.code)
    elif hasattr(e,"reason"):
        print("URLError")
        print(e.reason)

print("ok")

'''
url = "http://www.sfgsdg.com"
req = request.Request(url)
try:
    res = request.urlopen(req)
    html = res.read().decode("utf-8")

    print(len(html))
except error.HTTPError as e:
    print("HTTPError")
    print(e.reason)
    print(e.code)
except error.URLError as e:
    print("URLError")
    print(e.reason)

print("ok")
'''