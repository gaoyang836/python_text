*** Settings ***
Library    cases/c001001.py   WITH NAME  C001001
Library    cases/c001002.py   WITH NAME  C001002
Library    cases/c001003.py   WITH NAME  C001003


*** Test Cases ***

添加老师1 - tc001001
    #sleep 1d
    [Setup]    C001001.setup    #需要初始化删掉所有老师
    C001001.steps
    [Teardown]   C001001.teardown


添加老师2 - tc001002
    [Setup]   C001002.setup     #空
    C001002.steps
    [Teardown]    C001002.teardown


添加老师3 - tc001003
    [Setup]   C001003.setup        #空
    C001003.steps
    [Teardown]    C001003.teardown



##修改

##删除