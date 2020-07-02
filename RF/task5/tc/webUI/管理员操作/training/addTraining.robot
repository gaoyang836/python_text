*** Settings ***
#Library  courselib.py
Resource  rflib/rc.robot
#Suite Setup     setupwebtest
#Suite Teardown   teardownwebtest
Library    Collections
Library    pylib.webAdmin

*** Test Cases ***
#添加培训班
#    [Setup]  WebAdmin.DeleteAll(training)
##    [Teardown]  deleteAllLesson
#    #loginwebsite
#    #addCourse   robot  RF框架
#    AddCourse   robot  RF框架   1
#    addTraining   培训班1   这是一个培训班    1   初中语文
#    checkTraining   培训班1
#    #close browser

添加培训班

    [Setup]   Run Keywords   DeleteAllTraining
    ...  AND  DeleteAllCourse
    ...  AND  AddCourse   初中语文    初中语文描述    1
    #...  AND  AddCourse   初中数学    初中数学    2

    AddTraining   培训班（初中班）   这是一个培训班     1   初中语文
    CheckTraining   培训班（初中班）

    [Teardown]    Run Keywords   DeleteAllTeacher
    ...  AND  DeleteAllCourse