# class AgeException(Exception):
#     def __init__(self, msg):
#         self.msg = msg


# class Person:
#     __age = None
#
#     def setAge(self, age):
#         self.__age = age
#
#     def getAge(self):
#         return self.__age
#
#     def Number(self):
#         if self.__age > 0:
#            print(self.getAge())
#         else:
#             raise AgeException('数据非法')
# a  =Person()
# a.setAge(0)
# try:
#     a.Number()
# except AgeException as e:
#     print(e)

class MoneyException(Exception):
    def __init__(self, msg):
        self.msg = msg


class bank:
    __money = 3000

    def getOver(self):
        return self.__money

    def getMoney(self, money):

        if money < self.getOver():
            last = self.getOver() - money
            print('取出金额为{}元卡上余额为{}元'.format(money,last))
        else:
            raise MoneyException('金额不足')


a = bank()
d = int(input('请输入取款金额'))
try:
    a.getMoney(d)
except MoneyException as e:
    print(e)
