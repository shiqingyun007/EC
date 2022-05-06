# _*_coding:utf-8_*_
# Author:Teacher shi
# Website:www.hzdledu.com
# Time:2022-04-18 15:33
# Software:PyCharm
# File:close_account.py


# 结算
class CloseAccount:
    def __init__(self, action):
        self.action = action

    # 点击结算
    def close_account(self):
        self.action.wait(3000).tap(None, 300, 370).wait(1000).tap(None, 300, 170).wait(1000). \
            tap(None, 100, 410).wait(1000).tap(None, 300, 260).wait(1000).tap(None, 600, 1050).wait(2000).perform()
