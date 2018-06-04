from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.zhihu.com/explore")

print(driver.get_cookies())

driver.add_cookie({'name':'namne','domain':'www.zhihu.com','value':'zhangsan'})

print(driver.get_cookies())

driver.delete_all_cookies()

print(driver.get_cookies())