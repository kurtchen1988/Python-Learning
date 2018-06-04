from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://www.baidu.com")

driver.execute_script("window.open()")

print(driver.window_handles)

driver.switch_to_window(driver.window_handles[1])

driver.get("https://www.taobao.com")

time.sleep(2)

driver.switch_to_window(driver.window_handles[0])

driver.get("https://www.jd.com")