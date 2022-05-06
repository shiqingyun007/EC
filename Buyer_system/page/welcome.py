# _*_coding:utf-8_*_
# Author:Teacher shi
# Website:www.hzdledu.com
# Time:2022-04-15 11:15
# Software:PyCharm
# File:welcome.py
import time
from selenium.webdriver.common.by import By


class Welcome:
    def __init__(self, driver):
        self.driver = driver

    # 欢迎界面5次左滑操作
    def welcome(self):
        # 判断是否在主页面
        flag = self.driver.find_elements(By.ID, 'com.insthub.ecmobile:id/toolbar_tabtwo') == []
        if flag:
            time.sleep(1)
            for i in range(5):
                time.sleep(1)
                self.driver.swipe(700, 640, 100, 640)
