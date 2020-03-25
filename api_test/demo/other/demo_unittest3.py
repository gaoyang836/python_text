# -*-coding:utf-8 -*-
# author:gaoyang time:2020-03-25

import unittest
from ddt import ddt,data
from lib.excelManage import readExcel,getNewExcel
import time
from lib.sendCourseRequest import sendCourseRequest
import json

# 读取测试用例
path = r'D:/python/api_test/data/教管系统-测试用例V1.2.xls'
# newExcel=getNewExcel(path)
list = readExcel(path,0)
# print(list)

@ddt
class UnittestDemo3(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls):
    #     pass
    #
    # @classmethod
    # def tearDownClass(cls):
    #     pass
    # #A.环境初始化方法【类级别的】
    @classmethod
    def setUpClass(cls):
        print('setUp方法运行了\r\n')

    #B.数据清除方法【类级别的】
    @classmethod
    def tearDownClass(cls):
        print('tearDown方法运行了\r\n')
    # 批量执行excel测试用例
    @data(*list)
    def test_excel(self,row):
        # print(row)
        dictBody = sendCourseRequest(row)
        time.sleep(0.001)
        test = json.loads(row[6])
        # print('>>>>用例运行了')

        if 'reason' in dictBody.keys():
            self.assertEqual(dictBody['retcode'], test['code'], dictBody['reason'])
        else:
            self.assertEqual(dictBody['retcode'], test['code'])
