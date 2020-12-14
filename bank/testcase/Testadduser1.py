import unittest
from blank.entity.bank import bank_addUser
from blank.entity.bank import bank
from ddt import ddt
from ddt import data
from ddt import unpack
from blank.untils.DateRead import DataRead

'''
   1.搞清楚哪些是要测的业务逻辑部分
   2.写核心代码
   3.业务：
       用户满了：3
       已经存在：2
       开户成功：1
'''
data1 = DataRead('excel', filename='D:\\python\\blank\\testcase\\adduser1.xlsx', sheetname='0').list


@ddt
class TestBankAddUser(unittest.TestCase):
    @data(*data1)
    @unpack
    def testAddUser(self, username, password, country, province, street, door, money, status):
        for i in range(100):
            username = "张三" + str(i)
            # 实际结果
            bank_addUser(username, password, country, province, street, door, money)
        # 实际测试
        s = bank_addUser(username=username, password=password, country=country, province=province, street=street,
                         door=door, money=money)
        bank.clear()
        # 断言
        self.assertEqual(status, s)
