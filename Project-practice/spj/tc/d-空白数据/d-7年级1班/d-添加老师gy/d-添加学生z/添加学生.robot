*** Settings ***
Library    cases/c002001.py   WITH NAME  C002001
Library    cases/c002002.py   WITH NAME  C002002
Library    cases/c002081.py   WITH NAME  C002081


*** Test Cases ***

添加学生1 - tc002001
    # sleep  1d
    [Setup]    C002001.setup         #删掉所有学生
    C002001.steps                    #添加一个学生
    [Teardown]   C002001.teardown    #删掉所有学生


添加学生2 - tc002002
    [Setup]   C002002.setup          #空
    C002002.steps                    #添加一个学生
    [Teardown]    C002002.teardown   #删掉所有学生


删除学生3 - tc002081
    [Setup]   C002081.setup          #空
    C002081.steps                    #添加一个学生，删学生
    [Teardown]    C002081.teardown   #删掉所有学生


