*** Settings ***
Library  testlib3.py
#Library  Dialogs
Library  Collections  #RF操作列表和字典的一个库

*** Test Cases ***
#case1
#    FOR  ${one}  IN RANGE  9999
#    ${score}    get value from user    请输入分数
#    # 当用户输入over时候，结束循环-break
#    run keyword if   $score=='over'   exit for loop
#    #当用户输入cont时候，重新开始循环-continue
#    run keyword if   $score=='cont'  continue for loop
#    check score   ${score}
#    END
#
#case2
#    FOR  ${one}  IN RANGE  9999
#    ${score}    get value from user    请输入分数
#    # 当用户输入over时候，结束循环-break
#    exit for loop if   $score=='over'
#    #当用户输入cont时候，重新开始循环-continue
#    continue for loop if   $score=='cont'
#    check score   ${score}
#    END
#case3
#    ${list}  create list   1  2   3
#    log to console  ${list}
#    append to list  ${list}   a   b    c
#    log to console  ${list}
#    remove from list  ${list}    0  #删除第1个元素
#    log to console  ${list}
case4
#    ${list}   evaluate  [i for i in range(10) if i%2==0]
#    ${list}   evaluate  [i for i in range(0,10,2) ]
    ${list}   evaluate   [i for i in range(100)]
    ${list}   evaluate   $list[:30]
    ${dict}   evaluate   {"a":'hello',"b":3}
    ${var1}   evaluate   $dict.update({"a":'world'})
    log to console  ${var1}
    log to console  ${dict}
    log to console  ${list}

