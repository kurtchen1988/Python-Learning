# 显式等待
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://www.zhihu.com/explore")

wait = WebDriverWait(driver,10)

input = wait.until(EC.presence_of_element_located((By.ID,"zu-top-add-question")))

print(input.text)