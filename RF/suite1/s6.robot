*** Settings ***
Suite Setup  log to console   执行套件初始化操作~
Suite Teardown   log to console   执行套件清除操作~

Test Setup  log to console   执行默认初始化操作*
Test Teardown   log to console   执行默认清除操作*
#为每个测试用例提供默认初始化清除操作

*** Test Cases ***
#用例的初始化清除
setupANDteardown
    #初始化和清除不必成对出现
    [Setup]   log to console   执行用例初始化操作
    #初始化报错只进行初始化和清除
    [Teardown]   log to console   执行用例清除操作
    log to console  执行用例主体  #测试用例主体报错不影响清除




