# _*_coding:utf-8_*_
# Author:Teacher shi
# Website:www.hzdledu.com
# Time:2022-04-15 10:03
# Software:PyCharm
# File:testcase01.py
import time
import unittest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from Buyer_system.flow.main_flow import MainFlow


class TestCase01(unittest.TestCase):
    def setUp(self) -> None:
        desired_caps = {
            "platformName": 'Android',  # 平台的名称
            'platformVersion': '7.1.2',  # 平台版本
            'deviceName': 'Android emulator',  # 设备名称
            'appPackage': 'com.insthub.ecmobile',  # 应用包名
            'appActivity': 'com.insthub.BeeFramework.activity.StartActivity',  # 应用acitivity名称
            'noReset': False,  # 重置缓存数据
            'unicodeKeyboard': True,  # 键盘支持中文输入
            'resetKeyboard': True
        }

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.action = TouchAction(self.driver)
        self.driver.implicitly_wait(4)
        # self.driver.find_element_by_accessibility_id('name的值')

    def test(self):
        MainFlow(self.driver, self.action).main_flow()

    def tearDown(self) -> None:
        time.sleep(3)
        self.driver.quit()
