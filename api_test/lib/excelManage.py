# -*-coding:utf-8 -*-
# author:gaoyang time:2020-03-18

import xlrd
from xlutils.copy import copy  # 复制带格式
# 读取excel中的数据-----------------------------
def readExcel(filePath,sheet_index):

    workBook=xlrd.open_workbook(filePath)  #得到整个excel

    workSheet = workBook.sheet_by_index(sheet_index) #得到具体表格
    # workSheet =workBook.sheet_by_name('课程管理')

    nrows=workSheet.nrows   # 获取行数
    print(nrows)

    listDate=[]
    for i in range(1,nrows):   #取每行数据--放入列表中
        row=workSheet.row_values(i)
        listDate.append(row)

    return listDate

# 复制excel函数-----------------------

def getNewExcel(filePath):
    workBook=xlrd.open_workbook(filePath,formatting_info=True)  #打开
    workBookNew=copy(workBook)    #复制
    return workBookNew


# 调用函数
if __name__ =='__main__':

    #绝对路径
    # list=readExcel(r'D:\python\api_test\data\教管系统-测试用例V1.2.xls',0)

    #相对路径
    list=readExcel(r'../data/教管系统-测试用例V1.2.xls',0)
    # print(list)
