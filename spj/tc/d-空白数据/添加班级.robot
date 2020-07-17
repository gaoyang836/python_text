*** Settings ***
Library  pylib.SchoolClasslib

*** Test Cases ***
 添加班级1 - tc000001
    ${addRet}=  add school class   1    1班   60
    should be true  $addRet['retcode']==0

    ${listRet}=  list school class    1
    ${fc}=  evaluate    $listRet['retlist'][0]
    should be true  $fc['id']==$addRet['id']
    should be true  $fc['invitecode']==$addRet['invitecode']
    should be true  $fc['grade_name']=='七年级'
    should be true  $fc['studentlimit']==60
    should be true  $fc['name']=='1班'

    [Teardown]   delete_school_class   &{addRet}[id]