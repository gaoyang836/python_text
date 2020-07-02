# -*-coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from cfg import *
import time


class WebAdmin():
    # 保证仅实例化一次
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    #定义rf初始化操作

    def setWebTest(self,driverType='chrome'):
        # self.cur_wd 保存 webDriver 对象
        self.cur_wd = None
        if driverType == 'chrome':
            self.cur_wd = webdriver.Chrome()
        else:
            raise Exception('unknow driver type %s' % driverType)
        #隐式等待
        self.cur_wd.implicitly_wait(10)


    def tearDownWebTest(self):
        #关闭浏览器
        self.cur_wd.quit()

    def DeleteAllCourse(self):

        self.cur_wd.find_element_by_css_selector('ul.nav a[ui-sref=course]').click()
        time.sleep(1)

        self.cur_wd.implicitly_wait(2)
        while True:
            delButtons = self.cur_wd.find_elements_by_css_selector('*[ng-click^=delOne]')

            if delButtons == []:
                break

            delButtons[0].click()
            self.cur_wd.find_element_by_css_selector('.modal-footer  .btn-primary').click()
            time.sleep(1)

        self.cur_wd.implicitly_wait(10)


    def DeleteAllTeacher(self):

        self.cur_wd.find_element_by_css_selector('ul.nav a[ui-sref=teacher]').click()
        time.sleep(1)

        self.cur_wd.implicitly_wait(2)
        while True:
            delButtons = self.cur_wd.find_elements_by_css_selector('*[ng-click^=delOne]')

            if delButtons == []:
                break

            delButtons[0].click()
            self.cur_wd.find_element_by_css_selector('.modal-footer  .btn-primary').click()
            time.sleep(1)

        self.cur_wd.implicitly_wait(10)


    def DeleteAllTraining(self):

        self.cur_wd.find_element_by_css_selector('ul.nav a[ui-sref=training]').click()
        time.sleep(1)

        self.cur_wd.implicitly_wait(2)
        while True:
            delButtons = self.cur_wd.find_elements_by_css_selector('*[ng-click^=delOne]')

            if delButtons == []:
                break

            delButtons[0].click()
            self.cur_wd.find_element_by_css_selector('.modal-footer  .btn-primary').click()
            time.sleep(1)

        self.cur_wd.implicitly_wait(10)

    def DeleteAllTrainingGrade(self):

        self.cur_wd.find_element_by_css_selector('ul.nav a[ui-sref=traininggrade]').click()
        time.sleep(1)

        self.cur_wd.implicitly_wait(2)
        while True:
            delButtons = self.cur_wd.find_elements_by_css_selector('*[ng-click^=delOne]')

            if delButtons == []:
                break

            delButtons[0].click()
            self.cur_wd.find_element_by_css_selector('.modal-footer  .btn-primary').click()
            time.sleep(1)

        self.cur_wd.implicitly_wait(10)

    # delete_xxx 基本差不多，可以考虑抽象为一个通用的,后面delete班，班期 就不用开发关键字函数了
    def DeleteAll(self,objName):
        if objName=='course':
            self.cur_wd.find_element_by_css_selector('ul.nav a[ui-sref=course]').click()
        elif objName=='teacher':
            self.cur_wd.find_element_by_css_selector('ul.nav a[ui-sref=teacher]').click()
        elif objName=='training':
            self.cur_wd.find_element_by_css_selector('ul.nav a[ui-sref=training]').click()
        elif objName == 'traininggrade':
            self.cur_wd.find_element_by_css_selector('ul.nav a[ui-sref=traininggrade]').click()
        else :
            raise Exception('keyword DeleteAll get unknow obj Name %s' % objName)

        self.cur_wd.implicitly_wait(2)
        while True:
            delButtons = self.cur_wd.find_elements_by_css_selector('*[ng-click^=delOne]')

            if delButtons == []:
                break

            delButtons[0].click()
            self.cur_wd.find_element_by_css_selector('.modal-footer  .btn-primary').click()
            time.sleep(1)

        self.cur_wd.implicitly_wait(10)


    #登录
    def loginWebSite(self):
        self.cur_wd.get(MgrLoginUrl)

        self.cur_wd.find_element_by_id('username').send_keys(adminuser['name'])
        self.cur_wd.find_element_by_id('password').send_keys(adminuser['pw'])

        self.cur_wd.find_element_by_tag_name('button').click()


    def AddCourse(self, name,desc,idx):
        self.cur_wd.find_element_by_css_selector('ul.nav a[ui-sref=course]').click()

        self.cur_wd.find_element_by_css_selector('button[ng-click^=showAddOne]').click()

        ele = self.cur_wd.find_element_by_css_selector("input[ng-model='addData.name']")
        ele.clear()
        ele.send_keys(name)

        ele = self.cur_wd.find_element_by_tag_name("textarea")
        ele.clear()
        ele.send_keys(desc)

        ele = self.cur_wd.find_element_by_css_selector("input[ng-model='addData.display_idx']")
        ele.clear()
        ele.send_keys(idx)

        self.cur_wd.find_element_by_css_selector('button[ng-click^=addOne]').click()

        time.sleep(1)


    def  AddTeacher(self,realname,username,desc,idx,lesson):
        self.cur_wd.find_element_by_css_selector('ul.nav a[ui-sref=teacher]').click()

        self.cur_wd.find_element_by_css_selector('button[ng-click^=showAddOne]').click()

        ele = self.cur_wd.find_element_by_css_selector(
            "input[ng-model='addEditData.realname']")
        ele.clear()
        ele.send_keys(realname)

        ele = self.cur_wd.find_element_by_css_selector(
            "input[ng-model='addEditData.username']")
        ele.clear()
        ele.send_keys(username)

        ele = self.cur_wd.find_element_by_css_selector(
            "textarea[ng-model='addEditData.desc']")
        ele.clear()
        ele.send_keys(desc)

        ele = self.cur_wd.find_element_by_css_selector(
            "input[ng-model='addEditData.display_idx']")
        ele.clear()
        ele.send_keys(idx)

        select = Select(self.cur_wd.find_element_by_css_selector(
            'select[ng-model*=courseSelected]'))
        select.select_by_visible_text(lesson)

        self.cur_wd.find_element_by_css_selector('button[ng-click*=addTeachCourse]').click()

        self.cur_wd.find_element_by_css_selector('button[ng-click^=addOne]').click()

        time.sleep(2)


    def  AddTraining(self,name,desc,idx,lesson):
        self.cur_wd.find_element_by_css_selector('ul.nav a[ui-sref=training]').click()

        self.cur_wd.find_element_by_css_selector('button[ng-click^=showAddOne]').click()

        ele = self.cur_wd.find_element_by_css_selector(
            "input[ng-model='addEditData.name']")
        ele.clear()
        ele.send_keys(name)

        ele = self.cur_wd.find_element_by_css_selector(
            "textarea[ng-model='addEditData.desc']")
        ele.clear()
        ele.send_keys(desc)

        ele = self.cur_wd.find_element_by_css_selector(
            "input[ng-model='addEditData.display_idx']")
        ele.clear()
        ele.send_keys(idx)

        select = Select(self.cur_wd.find_element_by_css_selector(
            'select[ng-model*=courseSelected]'))
        select.select_by_visible_text(lesson)

        #self.cur_wd.find_element_by_css_selector('button[ng-click*=addTeachCourse]').click()

        self.cur_wd.find_element_by_css_selector('button[ng-click^=addOne]').click()

        time.sleep(1)

    def AddTrainingGrade(self,name,desc,idx,training):
        self.cur_wd.find_element_by_css_selector('ul.nav a[ui-sref=traininggrade]').click()

        self.cur_wd.find_element_by_css_selector('button[ng-click^=showAddOne]').click()

        ele = self.cur_wd.find_element_by_css_selector(
            "input[ng-model='addEditData.name']")
        ele.clear()
        ele.send_keys(name)

        ele = self.cur_wd.find_element_by_css_selector(
            "textarea[ng-model='addEditData.desc']")
        ele.clear()
        ele.send_keys(desc)

        ele = self.cur_wd.find_element_by_css_selector(
            "input[ng-model='addEditData.display_idx']")
        ele.clear()
        ele.send_keys(idx)

        select = Select(self.cur_wd.find_element_by_css_selector(
            'select[ng-model*=training_id]'))
        select.select_by_visible_text(training)

        self.cur_wd.find_element_by_css_selector('button[ng-click*=addTeachCourse]').click()

        self.cur_wd.find_element_by_css_selector('button[ng-click^=addOne]').click()

        time.sleep(1)

    def GetTeacherList(self):
        self.cur_wd.find_element_by_css_selector('ul.nav a[ui-sref=teacher]').click()

        # 试试 //tr/td[2]/span/text()
        eles = self.cur_wd.find_elements_by_css_selector('tr>td:nth-child(2)')

        return  [ele.text for ele in eles]


    def GetCourseList(self):
        self.cur_wd.find_element_by_css_selector('ul.nav a[ui-sref=course]').click()

        # 试试 //tr/td[2]/span/text()
        eles = self.cur_wd.find_elements_by_css_selector('tr>td:nth-child(2)')

        return  [ele.text for ele in eles]

    def GetTrainingList(self):
        self.cur_wd.find_element_by_css_selector('ul.nav a[ui-sref=training]').click()

        # 试试 //tr/td[2]/span/text()
        eles = self.cur_wd.find_elements_by_css_selector('tr>td:nth-child(2)')

        return  [ele.text for ele in eles]

    def GetTrainingGradeList(self):
        self.cur_wd.find_element_by_css_selector('ul.nav a[ui-sref=traininggrade]').click()

        # 试试 //tr/td[2]/span/text()
        eles = self.cur_wd.find_elements_by_css_selector('tr>td:nth-child(2)')

        return  [ele.text for ele in eles]

