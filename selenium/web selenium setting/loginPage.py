# -*-coding:utf-8 -*-
# author:gaoyang time:2020-04-08

from zidonghua.basePage import BasePage
from selenium.webdriver.common.by import By

# 页面类
class LoginPage(BasePage):
    def __init__(self):
        # 执行父类的执行方法
        super.__init__()
        # 用户名输入框元素
        self.userNameInput=(By.ID,"username")
        # 密码输入框元素
        self.passwordInput=(By.ID,"password")
        # 登录按钮
        self.loginButton=(By.TAG_NAME, "button")

    # 抽理出集体的元素控件
    def user_nameInputBox(self):
        return self.find_element(self.user_nameInput)

    def passwordInputBox(self):
        return self.find_element(self.passwordInput)

    def loginButtonBox(self):
        return self.find_element(self.button)


class LoginPageAction(LoginPage):

    def login(self):
        self.userNameInputBox().send_keys("auto")
        self.passwordInputBox().send_keys("sdfsdfsdf")
        self.loginButtonBox().click()