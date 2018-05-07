#爬取京东商品图片信息的案例
import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

#url
url = "https://list.jd.com/list.html?cat=9987,653,655"

#爬取数据
res = requests.get(url)
#print(res.text)
#
#使用BeautifulSoup解析数据
soup = BeautifulSoup(res.text,"lxml")

#获取图片信息
imlist = soup.find_all(name="img",attrs={'width':'220','height':'220'})
#print(len(imlist))
#
#遍历
m=1
for im in imlist:
    #判断当前图片的属性是否有src,并获取图片的url地址
    if "src" in im.attrs:
        imurl = "https:"+im.attrs['src']
    else:
        imurl = "https:"+im.attrs['data-lazy-img']
    #存储图片
    urlretrieve(imurl,"./mypic/p"+str(m)+".jpg")
    '''
    with requests.get(imurl,stream=True) as ir:
        with open("./mypic/p"+str(m)+".jpg","wb") as f:
            for chunk in ir:
                f.write(chunk)
    '''
    print("p"+str(m)+".jpg")
    m += 1