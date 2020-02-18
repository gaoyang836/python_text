#导入webdriver模块
from selenium import webdriver

#打开浏览器驱动和浏览器
#drive是webdriver的实例对象
drive=webdriver.firefox(r'd:\geckodriver.exe')
#等待时间
drive.implicitly_wait(10)
#打开网址
drive.get('http://www.51job.com')

#根据id的名称，找元素
#整个元素对应的对象
ele=drive.find_element_by_id('kwdselectid')
#在对象中输入内容
ele.send_keys('python')

#整个元素对应的对象
elec=drive.find_element_by_id('work_position_input')
#点击
elec.click()

#css表达式
eles=drive.find_element_by_css_selevtor('#work_position_click_center_right_list em[class=on]')

for ele in eles:
    ele.click()

drive.find_element_by_id('work_p....').click()


#搜索结果分析
jobs=drive.find_element_by_css_selevtor('#resultlist div[class=el]')

for job in jobs:
    fields=job.find_element_by_tag_name('span')
    stringFilelds=[field.text for field in fields]
    print('|'.join(stringFilelds))
