# author:gaoyang time:2020-03-02
# excel测试用例 接口自动化
# 待完善----------------------------------------------------------
import requests
import xlrd
import xlwt
import json

# 1.读excel数据
#添加文件路径
excelDir = r'd:\接口测试用例.xlsx'
#查看所有子表
# print(workBook.style_names())
workSheet=workBook.style_names()[1]
# workSheet=workBook.style_names('表名')

#读取一行
rows=workSheet.row_values(1)
#读取一列
# cols=workSheet.cell_values(0)
#读指定单元格
cellData=workSheet.cell(1,6).value #第二行第七列
# 返回当前单元格类型
# cellType=workSheet.cell(1,6).ctpe  # 返回1为str 2为int

# 2.构建请求
token_url=''
token_data={"uesrName":"gao","password":"123456"}  #请求参数
headers={"Content_Type":"application/json"}  #请求头
resp=requests.post(token_url,data=json,dumps(token_data),headers=headers)
token=resp.json()['token']  #获取token

# 新增用户
addUser_url=''
addUser_data=json.loads(cellData)  #请求参数 单元格获取  字符串转字典
addUser_headers={"Content_Type":"application/json","X-AUTH-TOKEN":token}  #请求头
addUser_resp=requests.post(addUser_url,data=json,dumps(addUser_data),headers=addUser_headers)

res=addUser_resp.json()['message']
if res =='成功'
    print('成功',addUser_resp.elapsed.total_seconds())
    excal_res='pass'
else :
    print('失败')
    excal_res = 'fail'

# 3.测试结果excel

#import xlutils
from xlutils.copy import copy # 复制函数

#1-首先打开
workBookwr=xlrd.open_workbook(excalDir)
#2-复制
workBookwr=copy(workbook)
wrSheet=workBookwr.get_sheet(1)
wrSheet.write(1,9,excel_res) #写单元格
workBookwr.save(r'd:\接口测试用例结果.xlsx')








