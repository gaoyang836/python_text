import unittest

class UnittestDemo(unittest.TestCase):

    # A.环境初始化方法
    def setUp(self):
         print('setUp方法运行了')

    # B.数据清除方法【类级别的】
    def tearDown(self):
        print('tearDown方法运行了\r\n')

    #1. 测试用例1
    def test_001(self):
        print('>>>>用例1运行了')

    #4. 测试用例4
    def test_004(self):
        print('>>>>用例4运行了')

    #2. 测试用例2
    # @unittest.skip('不想执行的原因')
    def test_002(self):
        # for i in range():  # 循环中有报错不会继续执行，引入ddt
        #     pass
        self.assertEqual(1,2,'XX原因测试不通过')
        print('>>>>用例2运行了')

    #3. 测试用例3
    def test_003(self):
        print('>>>>用例3运行了')


