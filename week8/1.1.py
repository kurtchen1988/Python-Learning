from lxml import etree


f = open("./my.html",'r',encoding="utf-8")
content = f.read()
f.close()

html = etree.HTML(content)

result = html.xpath("/html/head/title/text()")
result = html.xpath("/html/body/h3/text()")
result = html.xpath("/html/body/h3/@id")
result = html.xpath("/html/body/ul/li")
result = html.xpath("//li")

print(result)

result = html.xpath("//li/a/@href")

print(result)
print("="*40)

result = html.xpath("//ul/li[1]/a/text()")
result = html.xpath("//ul/li[last()]/a/text()")
result = html.xpath("//ul/li[position()<3]/a/text()")
result = html.xpath("//ul/li[last()-2]/a/text()")
print(result)

print("="*40)

result = html.xpath("//li[1]/a/ancestor::*")
result = html.xpath("//li[1]/a/ancestor::ul")
result = html.xpath("//li[3]/a/attribute::*")
result = html.xpath("//li/a[@class='aa']/text()")
result = html.xpath("//table/tbody/child::tr[@class='tt']")
print(result)

print("="*40)

result = html.xpath("//li/a")

for v in result:
    print(v.xpath("text()")[0]+":"+v.xpath("@href")[0])
    print(v.text+":"+v.get('href'))