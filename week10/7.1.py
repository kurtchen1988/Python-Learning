# 前进和后退
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.get("https://www.taobao.com")
driver.get("https://www.jd.com")
time.sleep(2)
driver.back()
time.sleep(2)