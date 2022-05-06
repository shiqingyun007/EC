# _*_coding:utf-8_*_
# Author:Teacher shi
# Website:www.hzdledu.com
# Time:2022-04-15 17:03
# Software:PyCharm
# File:switch_module.py
from selenium.webdriver.common.by import By


class SwitchModule:
    def __init__(self, driver):
        self.driver = driver

    # 切换至搜索模块
    def switch_search(self):
        flag = self.driver.find_elements(By.ID, 'com.insthub.ecmobile:id/toolbar_tabtwo') != []
        if flag:
            self.driver.find_element(By.ID, 'com.insthub.ecmobile:id/toolbar_tabtwo').click()

    # 切换至个人中心
    def switch_person_center(self):
        flag = self.driver.find_elements(By.ID, 'com.insthub.ecmobile:id/toolbar_tabfour') != []
        if flag:
            self.driver.find_element(By.ID, 'com.insthub.ecmobile:id/toolbar_tabfour').click()
