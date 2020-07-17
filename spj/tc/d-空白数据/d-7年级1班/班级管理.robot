*** Settings ***
Library  pylib.SchoolClasslib

*** Test Cases ***
添加班级2 - tc000002
    ${addRet}=  add school class   1   2班   60
    should be true  $addRet['retcode']==0

    #列出班级
    ${listRet}=  list school class  1
    ${fc}=  evaluate    $listRet['retlist']
    #should be true  {"name":"2班","invitecode":$addRet['invitecode'],"studentlimit":60,"studentnumber":0,"grade_name":"七年级","id":$addRet['id'],"teacherlist":[]} in $fc
    classlist_should_contain    ${fc}
    ...   2班  七年级  ${addRet}[invitecode]   60   0  ${addRet}[id]

    [Teardown]   delete_school_class   &{addRet}[id]


添加班级3 - tc000003
    ${listBefore}=  list school class    1

    ${addRet}=  add school class   1    1班   60
    should be true  $addRet['retcode']==1
    should be true  $addRet['reason']=="duplicated class name"

    ${listAfter}=  list school class    1
    should be equal   ${listBefore}  ${listAfter}



修改班级1 - tc000051
    ${addRet}=  add school class   1   2班   60
    should be true  $addRet['retcode']==0
    ${classid}=   evaluate  ${addRet}[id]

    ${modifyRet}  modify_scool_class    ${classid}   22班    60
    should be true  $modifyRet['retcode']==0

    #列出班级
    ${listRet}=  list school class  1
    ${fc}=  evaluate    $listRet['retlist']

    #should be true  {"name":"2班","invitecode":$addRet['invitecode'],
    #"studentlimit":60,"studentnumber":0,"grade_name":"七年级","id":$addRet['id'],"teacherlist":[]} in $fc
    classlist_should_contain    ${fc}
    ...   22班  七年级  ${addRet}[invitecode]   60   0  ${addRet}[id]

    [Teardown]   delete_school_class   &{addRet}[id]



修改班级2 - tc000052
    ${addRet}=  add school class   1   2班   60
    should be true  $addRet['retcode']==0
    ${classid}=   evaluate  ${addRet}[id]

    ${listBefore}=  list school class    1

    ${modifyRet}  modify_scool_class    ${classid}   1班    60
    should be true  $modifyRet['retcode']==1
    should be true  $addRet['reason']=="duplicated class name"

    ${listAfter}=  list school class    1
    should be equal   ${listBefore}   ${listAfter}

    [Teardown]   delete_school_class   &{addRet}[id]



修改班级3 - tc000053

    ${modifyRet}  modify_scool_class    999999999999   1班    60
    should be true  $modifyRet['retcode']==404
    should be true  $modifyRet['reason']=="id为'999999999999'的班级不存在"



删除班级1 - tc000081
    ${deleteRet}  delete_scool_class    999999999999
    should be true  $deleteRet['retcode']==404
    should be true  $deleteRet['reason']=="id为'999999999999'的班级不存在"



删除班级2 - tc000082

    ${addRet}=  add school class   1   2班   60
    should be true  $addRet['retcode']==0
    ${classid}=   evaluate  ${addRet}[id]

    ${listBefore}=  list school class    1
    classlist_should_contain   ${listBefore}[retlist]
    ...  2班  七年级  ${addRet}[invitecode]   60   0   ${addRet}[id]


    ${deleteRet}  delete_scool_class   ${classid}
    should be true  $deleteRet['retcode']==0


    ${listAfter}=  list school class    1
    #should be equal   ${listBefore}   ${listAfter}
    classlist_should_contain  ${listAfter}[retlist]
    ...  2班  七年级  ${addRet}[invitecode]   60   0   ${addRet}[id]   0
