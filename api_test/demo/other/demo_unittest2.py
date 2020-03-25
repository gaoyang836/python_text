import unittest

class UnittestDemo2(unittest.TestCase):

    #A.环境初始化方法【类级别的】
    @classmethod
    def setUpClass(cls):
        print('setUp方法运行了\r\n')

    #B.数据清除方法【类级别的】
    @classmethod
    def tearDownClass(cls):
        print('tearDown方法运行了\r\n')

    #1. 测试加法
    def test_001(self):
        print('>>>>用例1运行了')

    #2. 测试减法
    def test_002(self):
        print('>>>>用例2运行了')

    #3. 测试乘法
    def test_003(self):
        print('>>>>用例3运行了')

    #4. 测试除法
    def test_004(self):
        print('>>>>用例4运行了')
