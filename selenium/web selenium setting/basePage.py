# -*-coding:utf-8 -*-
# author:gaoyang time:2020-04-08

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from zidonghua.setting import driverPath,DOMIN,TIMEOUT,POLL_FREQUENCY

class Driver:
    # 静态私有字段
    _driver=None  # 类外不可访问
    # name=11       # 类外可访问

    # 类里面的函数叫方法，通过类.方法来访问
    @classmethod
    def get_driver(cls,brower_name="Chrome"):
        if cls._driver is None:
            if brower_name =="Chrome":
                cls._driver=webdriver.Chrome(driverPath["Chrome"])
            elif brower_name =="Firefox":
                cls._driver = webdriver.Firefox(driverPath["Firefox"])
            else:
                # 抛一个异常
                raise NameError("找不到浏览器")
        return cls._driver

class BasePage:
    def __init__(self):
        # 浏览器对象
        self.driver =Driver.get_driver()  # 调的类.方法
        # 访问网址
        self.get_url()                    # 调用内部方法
    def get_element(self,locator):
        # 显式等待，locator元素对象定位方法
        WebDriverWait(
            # 传入浏览器对象
            driver=self.driver,
            # 传入超时时间
            timeout=TIMEOUT,
            # 设置轮询时间
            poll_frequency=POLL_FREQUENCY
        ).until(
            # 定位元素是否可见
            ec.visibility_of_all_elements_located(locator))
        return self.driver.find_element(*locator)

    def get_url(self):
        self.driver.get(DOMIN)

if __name__=='__main__':
    from selenium.webdriver.common.by import By
    BasePage().get_element((By.ID,"username")).send_keys("123")
    # locator是(By.ID,"username")

