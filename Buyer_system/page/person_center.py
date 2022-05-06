# _*_coding:utf-8_*_
# Author:Teacher shi
# Website:www.hzdledu.com
# Time:2022-04-18 15:54
# Software:PyCharm
# File:person_center.py
from selenium.webdriver.common.by import By


class PersonCenter:
    def __init__(self, driver):
        self.driver = driver

    # 切换至设置模块
    def enter_setting(self):
        self.driver.find_element(By.ID, 'com.insthub.ecmobile:id/profile_setting').click()
