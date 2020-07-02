*** Settings ***
Library   course_mgr
Library   SeleniumLibrary

*** Test Cases ***
case1
    ${courses}  listCourse
    FOR  ${cour}   IN   @{courses}
    log to console   ${cour}
    END
    #should be true   ${courses}==['大学英语','大学物理']

case2
    open browser   https://www.vmall.com/   chrome
    set selenium implicit wait   10
    ${goods}   get webelements   css=.home-recommend-goods.home-hot-goods.grid-title
    ${res}  evaluate  [good.text for good in $goods]
    log to console  ${res}

    close browser