# _*_coding:utf-8_*_
# Author:Teacher shi
# Website:www.hzdledu.com
# Time:2022-04-15 15:43
# Software:PyCharm
# File:back.py


# 返回
import time

from selenium.webdriver.common.by import By


class Back:
    def __init__(self, driver):
        self.driver = driver

    # count为返回的次数
    def back(self, count):
        for i in range(count):
            time.sleep(3)
            self.driver.press_keycode(4)
        time.sleep(2)

    def back_homepage(self):
        while True:
            time.sleep(2)
            self.driver.press_keycode(4)
            # 判断是否有点亮的首页按钮
            flag = self.driver.find_elements(By.ID, 'com.insthub.ecmobile:id/toolbar_tabonebg') != []
            if flag:
                break  # 在页面，结束循环

            # 判断是否有首页的灰色按钮
            flag = self.driver.find_elements(By.ID, 'com.insthub.ecmobile:id/toolbar_tabone') != []
            if flag:
                self.driver.find_element(By.ID, 'com.insthub.ecmobile:id/toolbar_tabone').click()
                break
