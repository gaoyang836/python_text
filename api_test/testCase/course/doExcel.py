# -*-coding:utf-8 -*-
# author:gaoyang time:2020-03-20

import json
import time
from sendCourseRequest import sendCourseRequest
from excelManage import readExcel,getNewExcel

#执行测试用例，把结果写在excel表中--------------

path=r'../../data/教管系统-测试用例V1.2.xls'
savePath=r'../../report/测试结果2020-03-20.xls'

# 调用lib.excel_manage中readExcel函数，读内容
list = readExcel(path,0)

# 在新excel中，得到工作表
workBookNew=getNewExcel(path)
# workSheetNew=workBookNew.sheet_by_index(0)
workSheetNew = workBookNew.get_sheet(0)

# 循环执行每行用例
for i in range(0, len(list)):
    row=list[i]
    # 调sendCourceRequest函数，参数是excel每行的数据
    dictBody=sendCourseRequest(row)
    # dictBodys.append(dict)
    time.sleep(0.001)  #控制生成随机数的时间

    # 在新表写内容
    test=json.loads(row[6])  # 比对excel断言列
    if(dictBody['retcode']==test['code']):
        print(row[0],'测试通过')
        workSheetNew.write(i+1,7,'Pass')
    else:
        print(row[0],'测试失败')
        workSheetNew.write(i + 1,7,'Fall')

        if 'reason' in dictBody.keys():
            workSheetNew.write(i+1,8,dictBody['reason'])


# 保存整个excel
workBookNew.save(savePath)



