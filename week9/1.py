from scrapy import Selector

content = "<html><head><title>my page</title></head><body><h3>Hello scrapy</h3></body></html>"

selector = Selector(text=content)

print(selector.xpath('/html/head/title/text()').extract_first())

print(selector.css("h3::text").extract_first())