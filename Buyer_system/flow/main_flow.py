# _*_coding:utf-8_*_
# Author:Teacher shi
# Website:www.hzdledu.com
# Time:2022-04-15 15:39
# Software:PyCharm
# File:main_flow.py
import random
import unittest
from selenium.webdriver.common.by import By
from Buyer_system.common.back import Back
from Buyer_system.common.login import Login
from Buyer_system.common.register import Register
from Buyer_system.common.switch_module import SwitchModule
from Buyer_system.page.close_account import CloseAccount
from Buyer_system.page.config import Config
from Buyer_system.page.good_details import GoodDetails
from Buyer_system.page.goods_cart import GoodsCart
from Buyer_system.page.goods_list import GoodsList
from Buyer_system.page.home_page import HomePage
from Buyer_system.page.person_center import PersonCenter
from Buyer_system.page.search import Search
from Buyer_system.page.welcome import Welcome


class MainFlow(unittest.TestCase):
    def __init__(self, driver, action):
        super(MainFlow, self).__init__()
        self.driver = driver
        self.action = action

    def main_flow(self):
        Welcome(self.driver).welcome()  # 处理欢迎界面
        gl = GoodsList(self.driver, self.action)
        gd = GoodDetails(self.driver, self.action)
        num = random.randint(1, 2)
        # 随机进入商品列表
        if num == 1:
            HomePage(self.driver, self.action).random_enter_gl()  # 随机进入商品列表
        else:
            SwitchModule(self.driver).switch_search()  # 切换至搜索界面
            Search(self.driver).random_enter_gl()
        gl.load_resource()  # 上滑加载资源
        gl.search()  # 筛选商品
        gl.goods_sort()  # 按照“人气排行”对商品进行排序
        gl.enter_gd()  # 进入商品详情页
        gd.view_image()  # 查看图片
        gd.buy_now()
        Login(self.driver).enter_register()  # 在登录界面，进入注册界面
        Register(self.driver).register()  # 注册账号
        gd.buy_now()
        GoodsCart(self.driver, self.action).close_account()  # 在购物车中进行结算
        CloseAccount(self.action).close_account()  # 结算页面中进行结算操作
        flag = self.driver.find_elements(By.XPATH, "//android.widget.TextView[@text='购物车还没有商品']") != []
        self.assertTrue(flag)
        Back(self.driver).back_homepage()  # 返回首页
        SwitchModule(self.driver).switch_person_center()  # 切换至个人中心
        PersonCenter(self.driver).enter_setting()  # 切换至配置模块
        Config(self.driver).login_out()  # 执行注销操作
