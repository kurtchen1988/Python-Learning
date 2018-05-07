from pyquery import PyQuery as pq
import requests

#doc = pq(url="http://www.baidu.com", encoding="utf-8")

#print(doc('title').text())

#res = requests.get("http://www.baidu.com")
#res.encoding='utf-8'
#doc = pq(res.text)
#print(doc('title'))

f=open("./my.html","r", encoding="utf-8")
content = f.read()
f.close()

doc = pq(content)

#print(doc("h3"))
#print(doc("#hid"))
#print(doc(".aa"))
#print(doc(".shop"))
#print(doc("li a"))
print(doc("li:first"))
print(doc("li:last"))
print(doc("li:eq(2)"))
print("="*60)
print(doc("li").find("a.bb"))

alist = doc("a")

for a in alist.items():
    # print(a.text())
    print(a.html())
    print(a.attr("href"))
