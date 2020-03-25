import unittest
from demo.other.demo_unittest3 import UnittestDemo3
from ClassicHTMLTestRunner import HTMLTestRunner

#1 构建测试套件 test_suite
#1-1 方法一：用例逐个添加到suite
suite = unittest.TestSuite()  #类的实例化
# suite.addTest(UnittestDemo("test_001"))
# suite.addTest(UnittestDemo("test_003"))
# suite.addTest(UnittestDemo("test_002"))
# suite.addTest(UnittestDemo3("test_excel"))

#1-2 方法二：用例放入列表中，再添加到suite
# list=[UnittestDemo("test_001"),UnittestDemo("test_003")]
# suite.addTests(list)

#1-3 方法三：通过TestLoader类的discover 方法来
suite = unittest.defaultTestLoader.discover('demo.other', pattern="demo_unittest3.py")


#2 运行用例，查看结果
#2-1 第1种情况：使用unittest自带的报告导出
# runner=unittest.TextTestRunner()
# runner.run(suite)

#2-2 第2种情况：使用HTMLTestRunner
reportFile=open('./report/接口测试html报告.html','wb')
runner=HTMLTestRunner(tester='高杨',title='测试报告',
                      description='自动化接口测试报告',
                      stream=reportFile,
                      verbosity=2
                      )
runner.run(suite)
