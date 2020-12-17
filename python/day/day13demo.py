# def devide(a, b):
#     if b == 0:
#         raise ZeroDivisionError('被除数不能为0')
#     else:
#         print(a / b)
#
#
# try:
#     devide(6, 0)
#
# except ZeroDivisionError as e:
#     print('捕捉第一个异常', e)
# except ImportError as  e:
#     print('捕捉第二个异常', e)
# except Exception as e:
#     print('捕捉其他所有异常', e)


# class UserNotExixtsException(Exception):
#     def __init__(self, msg):
#         self.msg = msg
#
#
# raise UserNotExixtsException('用户信息不匹配')


class UserException(Exception):
    def __init__(self, msg):
        self.msg = msg


class User:
    __name = None
    __age = None

    def setAge(self, age):
        self.__age = age

    def getAge(self):
        return self.__age

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def compare(self, p):
        if self.__name == p.getName() and self.__age == p.getAge():
            print('同一个人')
        else:
            raise UserException('用户异常')


a = User()
a.setAge(56)
a.setName('张岩')
b = User()
b.setName('猴子')
b.setAge(56)

try:
    a.compare(b)
except UserException as e:
    print(e)