*** Settings ***
Resource  rflib/rc.robot
Library    pylib.webAdmin
Library    Collections
#Library   SeleniumLibrary
#Suite Setup  setupwebtest
#Suite Teardown  teardownwebtest
*** Test Cases ***
添加老师1

    [Setup]   Run Keywords   DeleteAllTeacher
    ...  AND  DeleteAllCourse
    ...  AND  AddCourse   初中语文    初中语文描述    1
    ...  AND  AddCourse   初中数学    初中数学    2

    AddTeacher   庄子    zhuangzi    庄子老师   1   初中语文
    ${teachers}=   GetTeacherList
    Should Be True    $teachers==[u'庄子']

    AddTeacher   孔子    kongzi    孔子老师   2   初中数学
    ${teachers}=   GetTeacherList
    Should Be True    $teachers==[u'庄子',u'孔子']

    [Teardown]    Run Keywords   DeleteAllTeacher
    ...  AND  DeleteAllCourse

添加老师
    [Setup]  run keywords   DeleteAllTeacher  AND  DeleteAllCourse
    ...  AND   Addcourse   初中语文  语文课  2
    #...  AND   Addcourse   初中数学  数学课  1

    AddTeacher   小张   xiaozhang  语文老师   1   初中语文
    CheckTeacher  小张

    [Teardown]  run keywords   DeleteAllTeacher   AND  DeleteAllCourse


##*** Keywords ***
#techersetup
#    deleteAllTeacher
#    deleteAllLesson
#    addcourse   初中语文  语文课  2
#    addcourse   初中数学  数学课  1

