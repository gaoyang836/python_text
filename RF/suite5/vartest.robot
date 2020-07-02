#变量文件
*** Settings ***
Variables   cfg.py

*** Test Cases ***
case1
    log to console   ${MgrLogUrl}
    log to console   ${StudentLoginUrl}
    log to console   ${database}
    log to console   ${user1}

