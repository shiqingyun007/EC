# _*_coding:utf-8_*_
# Author:Teacher shi
# Website:www.hzdledu.com
# Time:2022-04-18 11:29
# Software:PyCharm
# File:good_details.py
from selenium.webdriver.common.by import By


class GoodDetails:
    def __init__(self, driver, action):
        self.driver = driver
        self.action = action
        self.__inventory = None

    # 获取商品库存
    def get_inventory(self):
        good_property = self.driver.find_element(By.ID, 'com.insthub.ecmobile:id/good_property').text
        self.__inventory = good_property.split()[1].split('：')[1]
        return int(self.__inventory)

    # 查看商品图片
    def view_image(self):
        self.action.wait(2000).tap(None, 154, 317).wait(2000).tap(None, 360, 640). \
            wait(100).tap(None, 360, 640).wait(2000).tap(None, 45, 72).wait(2000).perform()

    # 立即购买
    def buy_now(self):
        self.driver.find_element(By.ID, 'com.insthub.ecmobile:id/buy_now').click()

        # 在点击立即购买时，判断是否有商品的属性弹出框
        flag = self.driver.find_elements(By.ID, 'com.insthub.ecmobile:id/shop_car_item_ok') != []
        if flag:
            # 点击弹出框的确认按钮
            self.driver.find_element(By.ID, 'com.insthub.ecmobile:id/shop_car_item_ok').click()
