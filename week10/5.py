from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.zhihu.com/explore")

driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
driver.execute_script('window.alert("Hello Seleium")')