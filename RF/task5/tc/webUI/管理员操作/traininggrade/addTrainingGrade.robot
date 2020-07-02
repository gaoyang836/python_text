*** Settings ***
#Library  courselib.py
Resource  rflib/rc.robot
#Suite Setup     setupwebtest
#Suite Teardown   teardownwebtest
Library    Collections
Library    pylib.webAdmin

*** Test Cases ***

添加培训班期

    [Setup]   Run Keywords   DeleteAllTrainingGrade
    ...  AND  DeleteAllTraining
    ...  AND  DeleteAllCourse
    ...  AND  AddCourse   初中语文    初中语文描述    1
    ...  AND  AddTraining   培训班（初中班）   这是一个培训班     1   初中语文


    AddTrainingGrade   培训班初中期   这是一个培训班期    1   培训班（初中班）
    CheckTrainingGrade   培训班初中期

    [Teardown]    Run Keywords   DeleteAllTrainingGrade
    ...  AND  DeleteAllTraining
    ...  AND  DeleteAllCourse


