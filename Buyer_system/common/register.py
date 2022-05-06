# _*_coding:utf-8_*_
# Author:Teacher shi
# Website:www.hzdledu.com
# Time:2022-04-18 11:36
# Software:PyCharm
# File:register.py
from selenium.webdriver.common.by import By


class Register:
    def __init__(self, driver):
        self.driver = driver

    # 读取注册文件中的第一条数据，注册新账号，将新账号的用户名写入用户信息文件中，删除第一条数据
    def register(self):
        with open(r'../data/register.csv', mode='r+') as file1:
            with open(r'../data/userinfo.txt', mode='a') as file2:
                lis = file1.readlines()
                userinfo = lis[0].rstrip('\n').split(',')
                username = userinfo[0]
                email = userinfo[1]
                file2.write(username + '\n')
                lis.pop(0)
                file1.seek(0, 0)
                file1.writelines(lis)
        self.driver.find_element(By.ID, 'com.insthub.ecmobile:id/register_name').send_keys(username)
        self.driver.find_element(By.ID, 'com.insthub.ecmobile:id/register_email').send_keys(email)
        self.driver.find_element(By.ID, 'com.insthub.ecmobile:id/register_password1').send_keys('123456')
        self.driver.find_element(By.ID, 'com.insthub.ecmobile:id/register_password2').send_keys('123456')
        self.driver.find_element(By.XPATH, "//android.widget.EditText[@text='MSN（必填*）']").send_keys(email)
        for index in range(1,5):
            self.driver.find_elements(By.ID, 'com.insthub.ecmobile:id/register_item_edit')[index].send_keys('123')
        self.driver.find_element(By.ID, 'com.insthub.ecmobile:id/register_register').click()
