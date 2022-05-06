# _*_coding:utf-8_*_
# Author:Teacher shi
# Website:www.hzdledu.com
# Time:2022-04-15 11:27
# Software:PyCharm
# File:home_page.py


#  主页
import random
import time

from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver, action):
        self.driver = driver
        self.action = action

    # 随机进入某商品的详情页
    def enter_gd(self):
        time.sleep(3)
        goods_list = self.driver.find_elements(By.XPATH,
                                               '//android.widget.ImageView[@resource-id="com.insthub.\
                                               ecmobile:id/good_cell_photo_two" or @resource-id="com.\
                                               insthub.ecmobile:id/good_cell_photo_three"]')
        random.choice(goods_list).click()

    def random_enter_gl(self):
        time.sleep(2)
        goods_list = self.driver.find_elements(By.ID, 'com.insthub.ecmobile:id/good_cell_photo_one')
        random.choice(goods_list).click()
        self.driver.get_screenshot_as_file(
            r'D:\Software\Python\ECMobile\Buyer_system\log\homepage%s.png' % time.strftime('%Y-%m-%d %H时%M分%S秒'))
