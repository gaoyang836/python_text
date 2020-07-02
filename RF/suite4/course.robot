# -*-coding:utf-8 -*-
*** Settings ***
Library   SeleniumLibrary
Library  courselib.py
*** Test Cases ***
添加课程
    [Setup]  deleteALLlesson
    [Teardown]  deleteALLlesson
    open browser   http://localhost/mgr/login/login.html   chrome
    set selenium implicit wait   5
    #登录
    input text    id=username   auto
    input text    id=password   sdfsdfsdf
    click element   css=.btn-success
    #添加课程
    click element   css=[ng-click="showAddOne=true"
    input text    css=[ng-model="addData.name"]   robot
    input text    css=[ng-model="addData.desc"]   RF框架
    #input text    css=input[ng-model="addData.display_idx"]    1
    click element  css=[ng-click="addOne()"]

    #检查添加的课程
    ${course}   get text  css=tbody td:nth-child(2)
    should be true   $course=='robot'
    close browser

添加课程2
    [Setup]  deleteALLlesson
    [Teardown]  deleteALLlesson
    open browser   http://localhost/mgr/login/login.html   chrome
    set selenium implicit wait   5
    #登录
    input text    id=username   auto
    input text    id=password   sdfsdfsdf
    click element   css=.btn-success
    #添加课程
    click element   css=[ng-click="showAddOne=true"
    input text    css=[ng-model="addData.name"]   selenium
    input text    css=[ng-model="addData.desc"]   webUI
    #input text    css=input[ng-model="addData.display_idx"]    1
    click element  css=[ng-click="addOne()"]

    #检查添加的课程
    ${course}   get text  css=tbody td:nth-child(2)
    should be true   $course=='robot'
    close browser