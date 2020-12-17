# class Person:
#     __usernaem = ''
#     __age = None
#
#     def setUsername(self, a):
#         self.__usernaem = a
#
#     def setAge(self, b):
#         if b == None:
#             print('年龄非法')
#         elif b > 120 or b < 0:
#             print('瞎巴巴啥')
#         else:
#             self.__age = b
#     def show(self):
#         print('我叫{}，年龄为{}'.format(self.__usernaem, self.__age))
#
# p = Person()
#
# p.setUsername('张岩')
# p.setAge(9999)
# p.show()
class Dog:
    __color = None
    __speed = None
    __belong = None

    def __init__(self, a, b, c):
        self.__color = a
        self.__speed = b
        self.__belong = c

    def setColor(self, a):
        self.__color = a

    def getColor(self):
        return self.__color

    def setSpeed(self, b):
        self.__speed = b

    def getSpeed(self):
        return self.__speed

    def setBelong(self, c):
        self.__belong = c

    def getBelong(self):
        return self.__belong

    def brand(self):
        print('颜色：{}，速度：{}，种类：{}'.format(self.__color, self.__speed, self.__belong))
d = Dog('红色','狗','50km/h')
d.brand()