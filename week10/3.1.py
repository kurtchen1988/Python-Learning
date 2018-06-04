from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.taobao.com")

input = driver.find_element_by_id("q")

input.send_keys('iphone')

time.sleep(3)

input.clear()

input.send_keys('ipad')

button = driver.find_element_by_class_name("btn-search")

button.click()