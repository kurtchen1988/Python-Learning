from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException

driver = webdriver.Chrome()
try:
    driver.get("https://www.baidu.com")
except TimeoutException:
    print("Time Out")


try:
    driver.find_element_by_id("demo")
except NoSuchElementException:
    print("No Element")
finally:
    pass