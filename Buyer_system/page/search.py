# _*_coding:utf-8_*_
# Author:Teacher shi
# Website:www.hzdledu.com
# Time:2022-04-15 17:00
# Software:PyCharm
# File:search.py
import random
import time

from selenium.webdriver.common.by import By

from Buyer_system.common.back import Back


class Search:
    def __init__(self, driver):
        self.driver = driver

    def random_enter_gl(self):
        while True:
            for i in range(2):
                category_list = self.driver.find_elements(By.ID, 'com.insthub.ecmobile:id/category_name')
                random.choice(category_list).click()
                time.sleep(1)
            flag = self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='没有结果']") == []
            # 判断是否有商品，如果有商品，结束循环
            if flag:
                break
            Back(self.driver).back(2)
