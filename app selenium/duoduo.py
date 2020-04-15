# -*-coding:utf-8 -*-
# author:gaoyang time:2020-04-15

#导包
from appium import webdriver

#准备自动化配置信息
desired_caps={
    #移动设备平台
    'platformName':'Android',
    #平台OS版本号
    'plathformVersion':'7',
    #设备的名称--值可以随便写
    'deviceName':'test0106',
    #提供被测app的信息-包名，入口信息
    'appPackage':'com.duoduocalca.calculator',
    'appActivity':'com.ego.shadow.CheckAppIdActivity',
    #确保自动化之后不重置app
    'noReset':True,
    #设置session的超时时间，单位秒
    'newCommandTimeout':6000,
    # appium 1.3的默认uiAutomator需要配置成2

    # 'automationName':'UiAutomator1'
    'skipServerInstallation':True
}

#初始化driver对象-用于控制手机
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(10)#稳定元素

ele3=driver.find_element_by_id('com.duoduocalca.calculator:id/cpp_button_3')
ele3.click()

plus=driver.find_element_by_id('com.duoduocalca.calculator:id/cpp_button_plus')
plus.click()

ele9=driver.find_element_by_id('com.duoduocalca.calculator:id/cpp_button_9')
ele9.click()

equal=driver.find_element_by_id('com.duoduocalca.calculator:id/cpp_button_equals')
equal.click()

ride=driver.find_element_by_id('com.duoduocalca.calculator:id/cpp_button_multiplication')
ride.click()

ele5=driver.find_element_by_id('com.duoduocalca.calculator:id/cpp_button_5')
ele5.click()

equal.click()

display=driver.find_element_by_id('com.duoduocalca.calculator:id/calculator_display')
text=display.text

if text=='60':
    print("测试通过")
else:
    print("测试不通过")
