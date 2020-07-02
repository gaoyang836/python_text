*** Settings ***
Variables   cfg.py

*** Keywords ***
loginwebsite
#    open browser   http://localhost/mgr/login/login.html   chrome
#    set selenium implicit wait   5
    #手动访问业务地址
    go to   ${MgrLogUrl}
    #登录
    input text    id=username    &{user1}[name]
    input text    id=password    &{user1}[pw]
    click element   css=.btn-success
addCourse
    #添加课程
    [Arguments]   ${name}   ${desc}   ${idx}=1
    click element   css=[ng-click="showAddOne=true"
    input text    css=[ng-model="addData.name"]   ${name}
    input text    css=[ng-model="addData.desc"]   ${desc}
    # input text    css=input[ng-model="addData.display_idx"]
    input text    css=input[ng-model="addData.display_idx"]     ${idx}
    click element  css=[ng-click="addOne()"]
checkCourse
    #检查添加的课程
    [Arguments]   ${expect}
    ${course}   get text  css=tbody td:nth-child(2)
    should be true   $course== $expect

#实现courselib.py中的deleteALLlesson
deleteALLlesson
    loginwebsite
    set selenium implicit wait  1
    #删除课程
    FOR  ${i}  IN RANGE   9999
        ${del_btns}   get webElements  CSS=[ng-click="delOne(one)"]
        #如果条件成立就退出循环
        exit for loop if  $del_btns==[]
        #点击删除按钮
        click element    ${del_btns[0]}
        #点击确认框
        click element    css=.btn-primary
        #等待弹出框消失
        sleep  1
    END
    set selenium implicit wait  10

#    close browser

setupwebtest
    open browser   http://baidu.com   chrome
    set selenium implicit wait   10
    log to console  打开浏览器

teardownwebtest
    close browser
    log to console  关闭浏览器