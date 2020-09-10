*** Settings ***
Library    cases/c005001.py   WITH NAME  C005001

Variables  cfg.py



*** Test Cases ***

#老师登录1 - tc005001
#    [Setup]    C005001.setup   #空
#    C005001.steps   #一系列操作-创建老师、登录、点击班级学生菜单
#    [Teardown]   C005001.teardown  #删老师
#
