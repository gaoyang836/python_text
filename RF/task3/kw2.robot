*** Settings ***
Resource  rclib.robot    #导入资源文件

*** Test Cases ***
case
    ${res}  checklog3    2020
    log to console   ${res}