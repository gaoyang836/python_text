# -*-coding:utf-8 -*-
# author:gaoyang time:2020-03-31

# 题目--------------------------------------------------------
# 打开 12306 网站  https://kyfw.12306.cn/otn/leftTicket/init
# 出发城市 填写 ‘南京南’， 到达城市 填写 ‘杭州东’
# 发车时间 选 06:00--12:00
# 发车日期选当前时间的下一天，也就是日期标签栏的，第二个标签
# 我们要查找的是所有 二等座还有票的车次，打印出这些有票的车次的信息，结果如下：
# G7641
# G1505
# G7393
# G7689
#---------------------------------------------------------------

from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

# 打开 12306 网站  https://kyfw.12306.cn/otn/leftTicket/init
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get("https://kyfw.12306.cn/otn/leftTicket/init")

# 设置全屏（要不点不到发车时间）
driver.maximize_window()

# 出发城市 填写 ‘南京南’
start_input=driver.find_element_by_id("fromStationText")
start_input.click()
start_input.send_keys("南京南\n")
time.sleep(2)

# 到达城市 填写 ‘杭州东’
stop_input=driver.find_element_by_id("toStationText")
stop_input.click()
stop_input.send_keys("杭州东\n")
time.sleep(2)

# 1.css--------------------------------------------
# 发车时间 选 06:00--12:00
# 定位到下拉框元素     select标签适用
ele = driver.find_element_by_css_selector("div.pos-top>select")
# # 根据 value 属性选择
# Select(ele).select_by_value("06001200")
# 根据下拉框文本选择
Select(ele).select_by_visible_text("06:00--12:00")
time.sleep(2)

# 发车日期选当前时间的下一天，也就是日期标签栏的，第二个标签
sel = driver.find_element_by_css_selector("li.sel~li").click()
time.sleep(2)

# 查找的是所有 二等座还有票的车次
# 定位整个列表
# list = driver.find_elements_by_css_selector("#queryLeftTable td:nth-child(4)")
# 所有类型有座位的
seats = driver.find_elements_by_css_selector("#queryLeftTable>tr[class]")

for i in seats:
    # 迭代列表
    secondSeat = i.find_elements_by_css_selector("td")[3]
    # secondSeat = i.find_elements_by_css_selector("td:nth-child(4)")
    train = i.find_element_by_css_selector("a[title=\"点击查看停靠站信息\"]")

    if secondSeat.text in ["--", "候补"]:
        continue
    # print(train.text,secondSeat.text)
    print(train.text)

time.sleep(2)

# 2.xpath--------------------------------------------
# # 选时间
# Select(driver.find_element_by_xpath("//div/select")).select_by_visible_text("06:00--12:00")
# # 选下一天
# driver.find_element_by_xpath("//div[@id=\"date_range\"]/ul/li[2]")
# # 选二等座
# seats=driver.find_elements_by_xpath("//tr/td[4]")
# # 选车牌
# for seat in seats:
#     if seat.text in ["--", "无", "候补"]:
#         continue
#     print(seat.find_element_by_xpath("./..//a[@title =\"点击查看停靠站信息\"]").text)



    # 关闭
driver.quit()






