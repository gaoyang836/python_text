# -*-coding:utf-8 -*-
*** Settings ***
#Library   SeleniumLibrary
#Library  courselib.py
Resource  rflib/rc.robot
#Suite Setup     setupwebtest
#Suite Teardown   teardownwebtest
Library    Collections
Library    pylib.webAdmin

*** Test Cases ***

添加课程
    [Setup]  deleteAllCourse
    [Teardown]  deleteAllCourse
    #loginwebsite
    #addCourse   robot  RF框架
    AddCourse   robot  RF框架   1
    checkCourse   robot
    #close browser

添加课程2
    [Setup]  deleteAllCourse
    [Teardown]  deleteAllCourse
    #loginwebsite
    addCourse   selenium  webUI  2
    checkCourse   selenium
    #close browser

