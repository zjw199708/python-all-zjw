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
data1 = DataRead('excel', filename='D:\\python\\blank\\testcase\\adduser.xlsx', sheetname='0').list


@ddt
class TestBankAddUser(unittest.TestCase):
    @data(*data1)
    @unpack
    def testAddUser(self, username, password, country, province, street, door, money, status):
        # 实际结果
        s = bank_addUser(username=username, password=password, country=country, province=province, street=street,
                         door=door, money=money)
        bank.clear()
        # 断言
        self.assertEqual(status, s)

    # def testAddUser2(self):
    #     username = "李伟"
    #     password = 999
    #     country = "中国"
    #     province = "天津"
    #     street = "和平道"
    #     door = 101
    #     money = 1000
    #
    #     status = 2
    #     bank_addUser(username, password, country, province, street, door, money)
    #     s = bank_addUser("李伟", password, country, province, street, door, money)
    #     self.assertEqual(status, s)
