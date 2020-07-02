#如何定义用户关键字（封装用例步骤）
#*** Settings ***
#Library   SeleniumLibrary
#Library  courselib.py
*** Test Cases ***
case1
    # checklog
    # checklog2    2020    #参数
    ${res}  checklog3    2020
    log to console   ${res}


