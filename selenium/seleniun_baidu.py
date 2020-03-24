# -*-coding:utf-8 -*-
# author:gaoyang time:2020-03-23

from selenium import webdriver
import time

# 创建浏览器驱动（放环境变量就不要声明）
#driver = webdriver.Chrome("‪D:\python\\tool\chromedriver.exe")
# driver = webdriver.Chrome("‪D:\python\chromedriver.exe")
driver = webdriver.Chrome()
# 访问网址
driver.get('http://www.baidu.com')
# 找到搜索框
# inputElement=driver.find_element_by_id("kw")
# 元素定位1-id
# inputElement=driver.find_element_by_id("username")
#
# 元素定位2-clss属性
# buttonElement=driver.find_element_by_class_name("login")
#
# 元素定位3-name属性
# nameElement=driver.find_element_by_name("pd")
#
# 元素定位4-根据标签名字 <p>标签
# tagElement=driver.find_element_by_tag_name("p")

# 元素定位5-链接文本
linkElement=driver.find_element_by_link_text("抗击肺炎").click()

# 元素定位6-链接文本模糊搜索
linkmElement=driver.find_element_by_partial_link_text("抗击").click()

# 元素定位7-xpath 万能 定位到<li>a</li>
inputElement=driver.find_element_by_xpath("/html/body/div/ul[2]/li[1]").click()

# 元素定位8-css选择器 万能 copy selectr定位到<li>a</li>
inputElement=driver.find_element_by_css_selector("body > div > ul:nth-child(2) > li:nth-child(1)").click()

# 输入内容
inputElement.send_keys("松勤")

# 获取标签对中间的文本值
print(tagElement.text)

time.sleep(5)

# 点击搜索按钮

time.sleep(5)
# 释放资源
driver.quit()


















