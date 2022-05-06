# _*_coding:utf-8_*_
# Author:Teacher shi
# Website:www.hzdledu.com
# Time:2022-04-18 11:33
# Software:PyCharm
# File:login.py
from selenium.webdriver.common.by import By


class Login:
    def __init__(self, driver):
        self.driver = driver

    def login(self):
        self.driver.find_element(By.ID, 'com.insthub.ecmobile:id/login_name').send_keys("jack")
        self.driver.find_element(By.ID, 'com.insthub.ecmobile:id/login_password').send_keys("123456")
        self.driver.find_element(By.ID, 'com.insthub.ecmobile:id/login_login').click()

    # 进入注册界面
    def enter_register(self):
        self.driver.find_element(By.ID, 'com.insthub.ecmobile:id/login_register').click()

    def login_out(self):
        self.driver.find_element(By.ID, 'com.insthub.ecmobile:id/setting_exitLogin').click()
        self.driver.find_element(By.ID, 'com.insthub.ecmobile:id/yes').click()
