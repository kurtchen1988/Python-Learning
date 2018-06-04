from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()

url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
driver.get(url)

driver.switch_to.frame('iframeResult')

source = driver.find_element_by_css_selector("#draggable")
target = driver.find_element_by_css_selector("#droppable")

actions = ActionChains(driver)

actions.drag_and_drop(source,target)
time.sleep(3)

actions.perform()