from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pyquery import PyQuery as pq
from urllib.parse import quote

KEYWORD = "ipad"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(chrome_options=chrome_options)

wait = WebDriverWait(browser,10)

def index_page(page):
    print("正在爬取第", page, "页")
    try:
        url = 'https://s.taobao.com/search?q='+quote(KEYWORD)
        browser.get(url)
        if page > 1:
            input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'')))
            submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'')))
            input.clear()
            input.send_keys(page)
            submit.click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'')))
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'')))
        #get_products()
    except TimeoutException:
        index_page(page)

def main():
    '''遍历爬取每页信息'''
    for i in range(1,11):
        index(i)

if __name__ == '__main__':
    main()