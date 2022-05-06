# _*_coding:utf-8_*_
# Author:Teacher shi
# Website:www.hzdledu.com
# Time:2022-04-18 10:35
# Software:PyCharm
# File:goods_list.py
import random
import time

from selenium.webdriver.common.by import By

from Buyer_system.page.good_details import GoodDetails


class GoodsList:
    def __init__(self, driver, action):
        self.driver = driver
        self.action = action

    # 刷选商品
    def search(self):
        time.sleep(2)
        self.driver.tap([(650, 50)])
        self.action.wait(3000).tap(None, 450, 250).wait(1000). \
            tap(None, 250, 750).wait(1000).tap(None, 650, 70).wait(2000).perform()

    # 加载资源，上滑两次
    def load_resource(self):
        for i in range(2):
            time.sleep(3)
            self.driver.swipe(360, 1200, 360, 200)

    # 按照“人气排行”进行排序
    def goods_sort(self):
        time.sleep(2)
        self.driver.tap([(100, 130)])

    # 进入商品详情页
    def enter_gd(self):
        while True:
            # 选择任意商品进入商品详情页
            goods_list = self.driver.find_elements(By.ID, 'com.insthub.ecmobile:id/gooditem_photo')
            random.choice(goods_list).click()

            # 判断是否有库存
            flag = GoodDetails(self.driver,self.action).get_inventory() >= 1
            if flag:
                break

            # 如果没有库存，返回至商品列表，重新选择商品
            self.driver.press_keycode(4)
            time.sleep(2)
