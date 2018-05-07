from bs4 import BeautifulSoup

f = open("./my.html", "r", encoding="utf-8")
content = f.read()
f.close()

soup = BeautifulSoup(content, "lxml")

#print(soup.prettify())

#print(soup.title)
#print(soup.li)
#print(soup.a.attrs)
print(soup.a.attrs['href'])

print("="*50)

print(soup.li.a.string)
print(soup.li.a.name)

print(soup.find(name='li'))
print(soup.find(name='a'))
print(soup.find(attrs={'class':'aa'}))
print(soup.find_all(attrs={'class':'aa'}))
print(soup.find_all(name='a',attrs={'class':'aa'}))
print(soup.find_all(text='百度'))

print("="*50)

print(soup.select("li"))
print(soup.select("#hid"))
print(soup.select(".shop"))

list = soup.select("ul li a")
for v in list:
    print(v['href']+":"+v.string+v.get_text())