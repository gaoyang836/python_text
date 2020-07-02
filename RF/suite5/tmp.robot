*** Settings ***
Resource   vartest.robot

*** Test Cases ***
case1
    log to console   ${MgrLogUrl}
    log to console   ${StudentLoginUrl}
    log to console   ${database}
    log to console   ${user1}