*** Settings ***
Library    cases/c000001.py   WITH NAME  C000001
Library    cases/c000051.py   WITH NAME  C000051
Library    cases/c000052.py   WITH NAME  C000052
Library    cases/c000053.py   WITH NAME  C000053

Library    pylib.SchoolClassLib

*** Test Cases ***
添加班级1 - tc000001
    [Setup]   C000001.setup
    C000001.steps
    [Teardown]    C000001.teardown


修改班级1 - tc000051
    [Setup]   C000051.setup
    C000051.steps
    [Teardown]    C000051.teardown


修改班级2 - tc000052
    [Setup]   C000052.setup
    C000052.steps
    [Teardown]    C000052.teardown


修改班级3 - tc0000053
    [Setup]   C000053.setup
    C000053.steps
    [Teardown]    C000053.teardown














#*** Settings ***
#Library  pylib.SchoolClassLib
#
#*** Test Cases ***
#添加班级1 - tc000001
#    ${addRet}=   add_school_class    1    1班   60
#    should be true    $addRet['retcode']==0
#
#    ${listRet}=  list_school_class    1
#    ${fc}=  evaluate    $listRet['retlist'][0]
#    should be true  $fc['id']==$addRet['id']
#    should be true  $fc['invitecode']==$addRet['invitecode']
#    should be true  $fc['grade__name']=='七年级'
#    should be true  $fc['studentlimit']==60
#    should be true  $fc['name']=='1班'

#    [Teardown]   delete_school_class   &{addRet}[id]
