# -*-coding:utf-8 -*-
# author:gaoyang time:2020-03-28

from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

# 开始自动化---------------------------------------------
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("http://www.51job.com")

# 找到高级搜索框-------------------------------------------
input_element = driver.find_element_by_css_selector(
    "body > div.content > div > div.fltr.radius_5 > div > a").click()

# 填职能类别
driver.find_element_by_id("funtype_input").send_keys("高级软件工程师")

# 选公司性质
# 定位到下拉框元素
driver.find_element_by_id('cottype_list').click()
driver.find_element_by_css_selector('#cottype_list span.li[data-value="01"]').click()

# 选工作年限
driver.find_element_by_id('workyear_list').click()
driver.find_element_by_css_selector('#workyear_list span.li[data-value="02"]').click()

# 输入搜索内容
input=driver.find_element_by_id("kwdselectid")

# 输入搜索内容python
input.send_keys("python")
time.sleep(1)

# 修改城市

# 点开城市
click_city=driver.find_element_by_id("work_position_click").click()
time.sleep(1)

# 判断是否有默认城市，有的话取消
default_city=driver.find_element_by_class_name("panel_tags")
default=default_city.find_elements_by_tag_name("span")
if default:
    for i in range(len(default)-1):
        default[i].click()
    time.sleep(1)

# 选地区
# 打开h列
hlist=driver.find_element_by_css_selector("#work_position_click_center_left_each_220200")
hclick=hlist.click()
time.sleep(1)
# 打开杭州
hangzhou=driver.find_element_by_id("work_position_click_center_right_list_category_220200_080200").click()
time.sleep(1)
# 点击确定按钮
driver.find_element_by_id("work_position_click_bottom_save").click()
time.sleep(1)

# 点击搜索按钮  click_element
driver.find_element_by_css_selector(
    "body > div.container > div.d_lt.Fm > div.btnbox.p_sou > span").click()
time.sleep(1)

# 到达搜索界面，开始获取信息-----------------------------------

# 获取页数
page=driver.find_element_by_id("hidTotalPage")
page_int=int(page.get_attribute("value"))
# 加界面循环
for one in range(page_int):
    # 找到界面工作列表
    job_list=driver.find_element_by_id("resultList")
    # 定位每条数据
    jobs=job_list.find_elements_by_class_name("el")

    # 遍历当页每一条数据
    for i in jobs:
        # 出去标头一行
        # if "title" in i.get_attribute("class"):
        #     continue
        # 从span标签中，获取数据
        job=i.find_elements_by_tag_name("span")
        for i in job:
            oneline=i.text
            # 按行存到excel
            # for i in range(0, len(stringFilelds)):
            #     oneline = table.write(0, i, stringFilelds[i])
            print(oneline,end=" | ")

        print()

    # 切换下一页
    if page_int != 1:
        driver.find_element_by_css_selector(
            "#resultList > div.dw_page > div > div > div > ul > li:nth-child(8) > a")

# driver.quit()

