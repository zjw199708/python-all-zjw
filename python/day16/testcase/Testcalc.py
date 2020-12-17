import unittest
from ddt import data
from ddt import unpack
from ddt import  ddt
from day16.entity.Calc import Calc
from day16.untils.DataRead import DataRead

data1 = DataRead('excel',filename='D:\\python\\day16\\testcase\\qwer.xlsx',sheetname='0').list

@ddt
class TestCalc(unittest.TestCase):
    @data(*data1)
    @unpack
    def testAdd(self,a,b,c):
        ca =Calc()
        s = ca.add(a,b)

        self.assertEqual(s,c)
