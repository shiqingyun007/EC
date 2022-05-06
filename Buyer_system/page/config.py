# _*_coding:utf-8_*_
# Author:Teacher shi
# Website:www.hzdledu.com
# Time:2022-04-18 15:57
# Software:PyCharm
# File:config.py
from Buyer_system.common.login import Login


class Config:
    def __init__(self, driver):
        self.driver = driver

    def login_out(self):
        Login(self.driver).login_out()
