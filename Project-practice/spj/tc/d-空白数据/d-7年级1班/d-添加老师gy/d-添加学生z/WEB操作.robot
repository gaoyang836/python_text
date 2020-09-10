*** Settings ***
Library    cases/c005002.py   WITH NAME  C005002
Library    cases/c005101.py   WITH NAME  C005101
Variables  cfg.py


*** Test Cases ***

#老师登录2 - tc005002
#    [Setup]    C005002.setup        # 删除所有老师
#    C005002.steps                   # 一系列操作-创建老师、登录、点击班级学生菜单
#    [Teardown]   C005002.teardown   # 删除创建的老师


老师发布作业1 - c005101
    [Setup]   C005101.setup          #空
    #一系列操作-老师登录、发布作业，学生登录、完成作业，老师登录查看作业
    C005101.steps
    [Teardown]    C005101.teardown   #空

