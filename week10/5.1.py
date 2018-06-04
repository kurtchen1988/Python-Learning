from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.zhihu.com/explore")

logo = driver.find_element_by_id("zh-top-link-logo")

print(logo)
print(logo.get_attribute('class'))

input = driver.find_element_by_id("zu-top-add-question")
print(input.text)
print(input.id)
print(input.location)
print(input.tag_name)
print(input.size)