# -*-coding:utf-8 -*-
from selenium import webdriver
import time

def deleteAllLesson():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    #登录
    driver.get("http://localhost/mgr/login/login.html")
    #driver.find_element_by_id('username').send_keys('auto')
    #driver.find_element_by_id('password').send_keys('sdfsdfsdf')
    driver.find_element_by_css_selector('.btn-success').click()
    #删除课程
    driver.implicitly_wait(2)
    while True:
        deleteButtons = driver.find_elements_by_css_selector("button[ng-click^='delOne']")
        if deleteButtons:
            deleteButtons[0].click()
            driver.find_element_by_css_selector('button.btn-primary').click()
            time.sleep(1)
        else:
            break
    driver.implicitly_wait(10)

    driver.quit()

if __name__ == '__main__':
    deleteAllLesson()




