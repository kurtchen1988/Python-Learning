import time
from io import BytesIO
from PIL import Image
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

EMAIL = '122794105@qq.com'
PASSWORD = 'python123'
BORDER = 6

class CrackGeetest():
    def __init__(self):
        self.url = 'https://account.geetest.com/login'
        self.browser = webdriver.Chrome()
        #设置显示等待
        self.wait = WebDriverWait(self.browser, 20)
        self.email = EMAIL
        self.password = PASSWORD

    def __del__(self):
        pass

    def get_geetest_button(self):
        # 获取初始验证按钮，return:按钮对象
        button = self.wait.until(EC.element_located_to_be_clickable((By.CLASS_NAME,'geetest_radar_tip')))
        return button

    def get_position(self):
        # 获取验证码位置，reuturn：验证码位置(元组)
        img = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'geetest_canvas_img')))
        time.sleep(2)
        location = img.location
        size = img.size
        top, bottom, left, right = location['y'], location['y']+size['height'],location['x'],location['x']+size['width']
        return (top, bottom, left, right)

    def get_screenshot(self):
        # 获取网页截图，reutn：截图对象
        screenshot = self.browser.get_screenshot_as_png()
        screenshot = Image.open(BytesIO(screenshot))
        return screenshot

    def get_slider(self):
        # 获取滑块，return：滑块对象
        slider = self.wait.until(EC.element_located_to_be_clickable((By.CLASS_NAME, 'geetest_slider_button')))
        return slider

    def get_geetest_image(self, name='captcha.png'):
        # 获取验证码图片，return:验证码图像
        top, bottom, left, right = self.get_position()
        print('验证码位置', top, bottom, left, right)
        screenshot = self.get_screenshot()
        captcha = screenshot.crop((left, top, right, bottom))
        captcha.save(name)
        return captcha

    def open(self):
        # 打开网页输入用户名密码， return: None
        self.browser.get(self.url)
        email = self.wait.until(EC.presence_of_element_located((By.ID,'email')))
        password = self.wait.until(EC.presence_of_element_located((By.ID,'password')))
        email.send_key(self.email)
        password.send_key(self.password)

    def get_gap(self,image1,image2):
        # 获取缺口偏量，参数：image1不带缺口图片，image2带缺口图片。返回偏移量
        left= 65


    def crack(self):
        # 输入用户名密码
        self.open()

        # 点击验证按钮


# 主程序入口
if __name__ == '__main__':
    crack = CrackGeetest()
