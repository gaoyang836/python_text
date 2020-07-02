*** Settings ***
Library   t1
*** Test Cases ***

#自定义库
#    ${var3}    set variable     wu
#    ${type}    get type   ${var3}
#    log to console  ${type}
#
#    ${list}    get list
    #log to console  ${list}
    #log to console  @{list}[0]
    #log to console  @{list[0]}
    #log to console  @{dict['key1']}
#
#循环1旧
#    :FOR  ${var}    IN     a   b   c   d
#    \   log to console   ${var}
#    log to console   循环外
#
#循环2新
#    FOR  ${var1}    IN     a   b   c   d
#    log to console   ${var1}
#    END   #出循环
#    log to console   循环外
#
#循环2新
#    ${list}    get_list
#    FOR  ${var2}  IN   @{list}
#    log to console   ${var2}
#    END   #出循环
#    log to console   循环外
#
#循环的range
#    FOR  ${var2}  IN RANGE   10
#    #FOR  ${var2}  IN RANGE   1  10  2
#    log to console   ${var2}
#    END   #出循环
#    log to console   循环外
#
#模拟while循环
#    FOR  ${var2}  IN RANGE     99999
#    log to console   ${var2}
#    #加判断循环
#    END

条件判断
    ${year}   set variable  2020
#    run keyword if   10>9   log to console   测试通过
#    run keyword if   ${year}=='2020'   log to console   测试通过
    run keyword if   ${year}==2020     log to console   测试通过1
    #should be true   ${year}=='2020'   log to console   测试通过2
    should be true   $year=='2020'

条件判断2
    ${date}   get time
    run keyword if   '2020' in $date and '05' in $date
    ...    log to console  pass
    log to console  ${date}

条件判断3分支
    ${date}   get time
    run keyword if   '2021' in $date  log to console  今年是2021年
    ...   ELSE    log to console  今年不是2021

条件判断4多分支
    ${date}   get time
    run keyword if   '2021' in $date  log to console  今年是2021年
    ...   ELSE IF   '05' in $date   log to console  这是5月
    ...   log to console  今年不是2021年也不是五月







