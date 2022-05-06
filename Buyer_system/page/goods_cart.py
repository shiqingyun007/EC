# _*_coding:utf-8_*_
# Author:Teacher shi
# Website:www.hzdledu.com
# Time:2022-04-18 14:27
# Software:PyCharm
# File:goods_cart.py
from selenium.webdriver.common.by import By

from Buyer_system.common.add_address import AddAddress


class GoodsCart:
    def __init__(self, driver, action):
        self.driver = driver
        self.action = action

    def close_account(self):
        self.driver.find_element(By.ID, 'com.insthub.ecmobile:id/shop_car_footer_balance').click()

        # 判断是否需要添加收货地址
        flag = self.driver.find_elements(By.ID, 'com.insthub.ecmobile:id/add_address_name') != []
        if flag:
            AddAddress(self.driver, self.action).add_address()
            self.driver.find_element(By.ID, 'com.insthub.ecmobile:id/shop_car_footer_balance').click()
