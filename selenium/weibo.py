# -*-coding:utf-8 -*-
# author:gaoyang time:2020-03-24

from selenium import webdriver
import time

# 创建浏览器驱动
driver = webdriver.Chrome()

# 访问网址
driver.get('https://m.weibo.cn/')
time.sleep(1)
# 点击大家都在搜
everyoneSearch = driver.find_element_by_class_name("m-text-cut").click()
# linkElement=driver.find_element_by_partial_link_text("大家都在搜：").click()
time.sleep(1)
# 找到并点击微博热搜榜 *******************************************
# driver.find_element_by_css_selector("#app > div:nth-child(1) > div:nth-child(1) > div.card.m-panel.card16.m-col-2 > div > div > div:nth-child(8) > div").click()
classElement = driver.find_element_by_class_name("m-col-2")
hotList=classElement.find_elements_by_class_name("m-item-box")[-1].click()
time.sleep(1)
# 找到实时热点，每分钟更新一次
hotSpot=driver.find_element_by_css_selector(
    "#app > div:nth-child(1) > div:nth-child(1) > div:nth-child(2)")
time.sleep(1)
# 找到每条热搜信息
#hotInformation = hotSpot.find_elements_by_class_name("card m-panel card4")
hotInformation = hotSpot.find_elements_by_class_name("card4")
# 将带有 热、沸、新字样的热搜信息获取并分类------------------
 # 遍历每条热搜信息
for hot in hotInformation:
    # 判断有无小图标
    hotPictures=hot.find_elements_by_class_name("m-link-icon")
    if hotPictures:
        # 取热搜信息内容********************************************
        img = hotPictures[0].find_element_by_tag_name("img")
        srcText=img.get_attribute("src")
        hotText = hot.find_element_by_class_name("m-text-cut").text
        # 取图片信息中的信息进行判断
        if 'hot' in srcText:
            print("热:",hotText)
        elif 'new' in srcText:
            print("新:", hotText)
        elif 'fei' in srcText:
            print("沸:", hotText)

time.sleep(5)
#-----------------------------------------------------

# 释放资源
driver.quit()