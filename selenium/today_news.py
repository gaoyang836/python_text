# -*-coding:utf-8 -*-
# author:gaoyang time:2020-03-26

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.toutiao.com/")

#------用之前学的8中定位，只能取到左侧列表，不能取到更多中的内容-------------------------------------------

# 先定位到外层div
# hotNew=driver.find_element_by_css_selector("body > div > div.bui-box.container > div.bui-left.index-channel > div > div")
hotNew=driver.find_element_by_class_name("channel")

#取里面的li标签
# newList=hotNew.find_elements_by_class_name("channel-item")
newList=hotNew.find_elements_by_tag_name("li")


# 定义了一个函数取内容，存在一个列表里
def tlist (newList):
    list=[]
    for i in range(0,len(newList)-1):
        listText=newList[i].find_element_by_tag_name("span").text
        # 为什么这样listText后面的元素都是空的？？？取不到更多里面的内容
        # 只能先去掉空元素
        if listText:
            list.append(listText)
    # print(len(list))
    print(list)

tlist(newList)

#----用鼠标悬停------------------------------------------------

# 定位到‘更多’
above = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div/div/ul/li[13]/a/span")
# 鼠标悬停
ActionChains(driver).move_to_element(above).perform()
# 先找到表示整个列表的 ul 标签
ulList = driver.find_element_by_css_selector(
    "body > div > div.bui-box.container > div.bui-left.index-channel > div > div > ul")
# 寻找 ulList 当中的每一个每一个 span 标签
span = ulList.find_elements_by_tag_name("span")
for i in span:
    print(i.text)

#----------------------------------------------------

# 释放资源
driver.quit()