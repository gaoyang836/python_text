import unittest
from ddt import ddt,data

mydata2=[[5,4,1],[7,3,4]]

@ddt
class DemoDDT(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    @data(*mydata2)
    def test_001(self,data):
        print(data)

