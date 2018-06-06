from selenium import webdriver


service_args = [
    '--proxy=127.0.0.1:8888',
    '--proxy_type=http',
]

browser = webdriver.PhantomJS(service_args=service_args)

browser.get('http://httpbin.org/get')
print(browser.page_source)