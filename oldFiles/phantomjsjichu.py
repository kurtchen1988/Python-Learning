import time
from selenium import webdriver
browser = webdriver.PhantomJS()
#打开了一个PhantomJS浏览器
browser.get("https://www.baidu.com")
#get方法来直接访问网址
a=browser.get_screenshot_as_file("D:\\Python\\练习\\iofile\\test.jpg")
browser.find_element_by_xpath('//*[@id="kw"]').clear()
browser.find_element_by_xpath('//*[@id="kw"]').send_keys("爬虫")
browser.find_element_by_xpath('//*[@id="su"]').click()
time.sleep(5)
a=browser.get_screenshot_as_file("D:\\Python\\练习\\iofile\\test.jpg")
data=browser.page_source
browser.quit()
print(len(data))
import re
title=re.compile("<title>(.*?)</title>").findall(data)
print(title)
