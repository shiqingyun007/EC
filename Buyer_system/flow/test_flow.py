# _*_coding:utf-8_*_
# Author:Teacher shi
# Website:www.hzdledu.com
# Time:2022-04-15 16:56
# Software:PyCharm
# File:test_flow.py

import time

from Buyer_system.page.home_page import HomePage
from Buyer_system.page.welcome import Welcome


class TestFlow:
    def __init__(self, driver, action):
        self.driver = driver
        self.action = action

    def test_flow(self):
        Welcome(self.driver).welcome()  # 处理欢迎界面
        HomePage(self.driver, self.action).random_enter_gl()  # 随机进入商品列表
        time.sleep(3)
        dic = self.driver.get_window_size()
        width = dic["width"]
        height = dic["height"]
        self.driver.tap([(250 / 720 * width, 250 / 1280 * height)])

        self.driver.press_keycode(3)  # home操作

        self.driver.orientation = "LANDSCAPE"  # 横屏

        # 音量加减操作
        for i in range(5):
            self.driver.press_keycode(25)
            time.sleep(1)

        for i in range(5):
            self.driver.press_keycode(24)
            time.sleep(1)

        self.driver.orientation = "PORTRAIT"  # 竖屏
