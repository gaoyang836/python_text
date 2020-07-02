*** Settings ***
Library   SeleniumLibrary
Variables   cfg/cfg.py

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
    #确保在课程界面
    click element   css=[ui-sref="course"]
    #添加课程
    [Arguments]   ${name}   ${desc}   ${idx}=1
    click element   css=[ng-click="showAddOne=true"
    input text    css=[ng-model="addData.name"]   ${name}
    input text    css=[ng-model="addData.desc"]   ${desc}
    # input text    css=input[ng-model="addData.display_idx"]
    input text    css=input[ng-model="addData.display_idx"]     ${idx}
    click element  css=[ng-click="addOne()"]
checkCourse
    #确保在课程界面
    click element   css=[ui-sref="course"]
    #检查添加的课程
    [Arguments]   ${expect}
    ${course}   get text  css=tbody td:nth-child(2)
    should be true   $course== $expect

#实现courselib.py中的deleteALLlesson
deleteAllCourse
    #loginwebsite
    #确保在课程界面
    click element   css=[ui-sref="course"]
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


deleteAllTeacher
    # loginwebsite
    #开始删除老师
    click element  css=[ui-sref="teacher"]
    #deleteALLlesson
    #开始删除课程
    set selenium implicit wait  2
    FOR  ${i}  IN RANGE   9999
        ${del_btns}   get webElements  CSS=[ng-click="delOne(one)"]
        #如果条件成立就退出循环
        exit for loop if  $del_btns==[]
        #点击删除按钮
        click element    ${del_btns[0]}
        #点击确认框
        click element    css=.btn-primary
        sleep  1
    END
    set selenium implicit wait  5

addTeacher
    #确保在老师界面
    click element  css=[ui-sref="teacher"]
    #添加老师
    [Arguments]   ${realname}  ${username}  ${desc}   ${idx}  ${course}
    click element   css=[ng-click="showAddOne=true"]
    input text    css=[ng-model="addEditData.realname"]   ${realname}
    input text    css=[ng-model="addEditData.username"]   ${username}
    input text    css=[ng-model="addEditData.desc"]   ${desc}
    input text    css=[ng-model="addEditData.display_idx"]  ${idx}
    #关联授课信息
    select from list by label  css=[ng-model="$parent.courseSelected"]  ${course}
    click element  css=[ng-click="addEditData.addTeachCourse()"]
    click element  css=[ng-click="addOne()"]

checkTeacher
    #确保在老师界面
    click element  css=[ui-sref="teacher"]
    #检查添加的课程
    [Arguments]   ${expect}
    ${course}   get text  css=tbody td:nth-child(2)
    should be true   $course== $expect



deleteAllTraining
    # loginwebsite
    click element  css=[ui-sref="training"]
    #deleteALLlesson
    set selenium implicit wait  2
    FOR  ${i}  IN RANGE   9999
        ${del_btns}   get webElements  CSS=[ng-click="delOne(one)"]
        #如果条件成立就退出循环
        exit for loop if  $del_btns==[]
        #点击删除按钮
        click element    ${del_btns[0]}
        sleep  1
        #点击确认框
        click element    css=.btn-primary
        #等待弹出框消失
        sleep  2
    END
    set selenium implicit wait  5

addTraining
    #确保在老师界面
    click element  css=[ui-sref="training"]
    [Arguments]   ${name}    ${desc}   ${idx}  ${training}
    click element   css=[ng-click="showAddOne=true"]
    input text    css=[ng-model="addEditData.name"]   ${name}
    input text    css=[ng-model="addEditData.desc"]   ${desc}
    input text    css=[ng-model="addEditData.display_idx"]  ${idx}
    #关联授课信息
    select from list by label  css=[ng-model="$parent.courseSelected"]  ${training}
    click element  css=[ng-click="addEditData.addTeachCourse()"]
    click element  css=[ng-click="addOne()"]

checkTraining
    click element  css=[ui-sref="training"]
    [Arguments]   ${expect}
    ${training}   get text  css=tbody td:nth-child(2)
    should be true   $training== $expect




deleteAllTrainingGrade

    click element  css=[ui-sref="traininggrade"]
    set selenium implicit wait  2
    FOR  ${i}  IN RANGE   9999
        ${del_btns}   get webElements  CSS=[ng-click="delOne(one)"]
        #如果条件成立就退出循环
        exit for loop if  $del_btns==[]
        #点击删除按钮
        click element    ${del_btns[0]}
        sleep  1
        #点击确认框
        click element    css=.btn-primary
        #等待弹出框消失
        sleep  2
    END
    set selenium implicit wait  5


addTrainingGrade
    click element  css=[ui-sref="traininggrade"]
    #添加老师
    [Arguments]   ${name}   ${desc}   ${idx}  ${traininggrade}
    click element   css=[ng-click="showAddOne=true"]
    input text    css=[ng-model="addEditData.name"]   ${name}
    input text    css=[ng-model="addEditData.desc"]   ${desc}
    input text    css=[ng-model="addEditData.display_idx"]  ${idx}
    #关联授课信息
    select from list by label  css=[ng-model="$parent.addEditData.training_id"]  ${traininggrade}
    #click element  css=[ng-click="addEditData.addTeachCourse()"]
    click element  css=[ng-click="addOne()"]

checkTrainingGrade
    click element  css=[ui-sref="traininggrade"]
    #检查添加的课程
    [Arguments]   ${expect}
    ${traininggrade}   get text  css=tbody td:nth-child(2)
    should be true   $traininggrade== $expect

