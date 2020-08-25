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

*** Settings ***
Library    cases/c000001.py   WITH NAME  C000001

*** Test Cases ***

添加班级11 - tc0000011
    [Setup]   C000001.setup
    C000001.steps
    [Teardown]    C000001.teardown


