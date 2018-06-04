# 隐式等待
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(2)

driver.get("https://www.zhihu.com/explore")

input = driver.find_element_by_id("zu-top-add-question")

print(input.text)