*** Settings ***
Library  pylib.SchoolClasslib
Suite Setup   add school class   1    1班   60   suite_g7c1_classid
Suite Teardown  delete_school_classes   ${suite_g7c1_classid}

#------------------------------------------------------
#*** Keywords ***
#suite setup action
#    ${ret}= add school class    1    1班   60
#    set golbal variable   ${suite_g7c1_classid}    ${ret}[id]
#

#*** Settings ***
#Library  pylib.SchoolClasslib
#
#Suite Setup   ${suite_g7c1_classid}
#Suite Teardown   delete_school_classes   ${suite_g7c1_classid}

#删除的delete_school_classes中
#需要一个id进行删除用set golbal variable
#把add school class是生成的ID获取到，定义关键字，生成全局变量