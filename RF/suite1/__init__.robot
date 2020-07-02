#测试目录suite1下的初始化和清除
*** Settings ***
Suite Setup  log to console   执行目录初始化操作~
Suite Teardown   log to console   执行目录清除操作~

Test Setup  log to console   执行默认初始化操作*
Test Teardown   log to console   执行默认清除操作*