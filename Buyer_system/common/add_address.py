# _*_coding:utf-8_*_
# Author:Teacher shi
# Website:www.hzdledu.com
# Time:2022-04-18 14:42
# Software:PyCharm
# File:add_address.py
import time

from selenium.webdriver.common.by import By


class AddAddress:
    def __init__(self, driver, action):
        self.driver = driver
        self.action = action

    # 添加收货地址
    def add_address(self):
        with open(r'../data/userinfo.txt', mode='r') as file:
            username = file.read().split()[-1]
        self.driver.find_element(By.ID, 'com.insthub.ecmobile:id/add_address_name').send_keys(username)
        self.driver.find_element(By.ID, 'com.insthub.ecmobile:id/add_address_email').clear()
        self.driver.find_element(By.ID, 'com.insthub.ecmobile:id/add_address_email').send_keys(username+"@qq.com")
        self.driver.find_element(By.ID, 'com.insthub.ecmobile:id/add_address_telNum').send_keys('123123')
        self.driver.find_element(By.ID, 'com.insthub.ecmobile:id/add_address_zipCode').send_keys('123123')
        self.driver.find_element(By.ID, 'com.insthub.ecmobile:id/add_address_detail').send_keys('华星发展大厦')
        self.action.tap(None, 300, 470).wait(2000).tap(None, 80, 700).wait(2000).perform()
        for i in range(2):
            self.driver.swipe(360, 1100, 360, 250)
            time.sleep(1)
        self.action.tap(None, 80, 900).wait(2000).tap(None, 80, 320).wait(2000).tap(None, 100, 250).\
            wait(2000).tap(None, 400, 640).wait(2000).perform()
