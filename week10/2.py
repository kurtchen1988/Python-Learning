from selenium import webdriver

# driver = webdriver.Chrome()
# driver = webdriver.Firefox()
# driver = webdriver.Edge()
# driver = webdriver.Safari()
driver = webdriver.PhantomJS()
driver.get("http://www.taobao.com")
print(driver.page_source)