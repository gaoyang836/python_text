# -*-coding:utf-8 -*-
*** Settings ***
Library   SeleniumLibrary
#Library  courselib.py
Resource  rc.robot
Suite Setup     setupwebtest
Suite Teardown   teardownwebtest
*** Test Cases ***
添加课程
    [Setup]  deleteALLlesson
    [Teardown]  deleteALLlesson
    loginwebsite
    #addCourse   robot  RF框架
    addCourse   robot  RF框架   1
    checkCourse   robot
    #close browser

添加课程2
    [Setup]  deleteALLlesson
    [Teardown]  deleteALLlesson
    loginwebsite
    addCourse   selenium  webUI  2
    checkCourse   selenium
    #close browser



