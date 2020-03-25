# -*-coding:utf-8 -*-
# author:gaoyang time:2020-03-18

from excelManage import readExcel
import json
import time
from courseLib import course_add,course_delete,course_modify,course_list
import pprint


# 传excel行数据，执行并返回请求结果
def sendCourseRequest(row):
    # print(row)
    data = json.loads(row[5])  # 取到第六列的请求参数

    dictBody = []
    if (row[4] == 'add'):
        # 定义一个随机变量
        randomStr = str(int(time.time()))
        # 请求参数
        # data = json.loads(row[5])
        # 从请求参数中获取课程名称,把课程名称带变量标记的，替换为随机变量
        courseName = data['name'].replace('{{courseName}}', randomStr)
        # 发送课程新增请求
        dictBody = course_add(courseName, data['desc'], data['display_idx'])
    elif(row[4]=='list'):
        dictBody = course_list(data['pagenum'],data['pagesize'])
    elif(row[4]=='delete'):
        dictBody = course_delete(data['id'])
    # pprint.pprint(dictBody)

    # test=json.loads(row[6])
    # if(dictBody['retcode']==test['code']):
    #     print(row[0],'测试通过')
    # else:
    #     print(row[0],'测试失败')

    return dictBody

# if __name__ =='__main__':
    # # 调用lib.excel_manage中readExcel函数
    # list=readExcel(r'../data/教管系统-测试用例V1.2.xls',0)
    # # 循环执行每行用例
    # for i in range(0,len(list)):
    #     # 调SendCourceRequest函数，参数是excel每行的数据
    #     sendCourseRequest(list[i])
    #     time.sleep(0.001)  # 控制生成随机数的时间