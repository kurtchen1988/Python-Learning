from selenium import webdriver
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import re
import urllib.request

dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"]=("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                           "Chrome/50.0.2661.87 Safari/537.36")
#伪装浏览器，给PhantomJS加上一个header
browser = webdriver.PhantomJS(desired_capabilities=dcap)
browser.get("http://ac.qq.com/ComicView/index/id/539443/cid/1")
#browser.maximize_window()
a=browser.get_screenshot_as_file("D:\\Python\\练习\\iofile\\test.jpg")
#截屏,可以发现这样只能截取前三页。我们需要往下滑，然后才能得到想要数据
for i in range(10):
#这里循环就是滑动多少次的意思
    #browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    js='window.scrollTo('+str(i*1280)+','+str((i+1)*1280)+')'
    #按照分辨率计算，分别往下滑动多少像素
    browser.execute_script(js)
    time.sleep(1)
print(browser.current_url)
data=browser.page_source
fh=open("D:\\Python\\练习\\iofile\\dongman.html","w",encoding="utf-8")
fh.write(data)
fh.close()
browser.quit()

pat='<img src="(http://ac.tc.qq.com/store_file_download.buid=.*?name=.*?).jpg"'
allid=re.compile(pat).findall(data)

print(allid)

for i in range(0,len(allid)):
    thisurl=allid[i]
    thisurl2=thisurl.replace("amp;","")+".jpg"
    localpath="D:\\Python\\练习\\iofile\\"+str(i)+".jpg"
    urllib.request.urlretrieve(thisurl,filename=localpath)