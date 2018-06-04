from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.taobao.com")

input = driver.find_element_by_id("q")

print(input)

input = driver.find_element_by_css_selector("#q")

print(input)

input = driver.find_element_by_xpath("//*[@id='q']")

print(input)

input = driver.find_element(By.ID,"q")

print(input)