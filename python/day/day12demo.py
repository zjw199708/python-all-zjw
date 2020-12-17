#
# class Phone:
#     phonenumber = None
#     voice = None
#     def call(self,number):
#         print('{}正在给{}打电话'.format(self.phonenumber,number))
#
#
# class Newphone(Phone):
#     place =None
#     picture = None
#     ps  = None
#     def call(self,number):
#         super().call(number)
#         print('归属地：{}，图片：{}，备注：{}'.format(self.place,self.picture,self.ps))
#
# oldphone = Phone()
# oldphone.phonenumber ='88456952'
# oldphone.voice = 'DJ喜羊羊'
# oldphone.call(213546)
# print('我的电话时{}，铃声是{}'.format(oldphone.phonenumber,oldphone.voice))
#
# newphone = Newphone()
# newphone.phonenumber=12138
# newphone.place='江苏'
# newphone.picture = 'zy傻叼'
# newphone.ps = '45222'
# newphone.call('124632')

import time


class Animal:
    __color = None
    __weight = None
    __age = None

    def __init__(self, color, weight, age):
        self.__color = color
        self.__weight = weight
        self.__age = age

    def setColor(self, color):
        self.__color = color

    def getColor(self):
        return self.__color

    def setweight(self, weight):
        self.__weight = weight

    def getWeight(self):
        return self.__weight

    def setAge(self, age):
        self.__age = age

    def getAge(self):
        return self.__age


class Dog(Animal):
    __brand = None

    def __init__(self, color, age, weight, brand):
        super().__init__(color, weight, age)
        self.__brand = brand

    def setBrand(self, brand):
        self.__brand = brand

    def getBrand(self):
        return self.__brand

    def show(self):
        for i in range(6):
            print('旺', end='')
            time.sleep(1)
        print('我是一只{}的狗，今年{}岁，最大体重为{}，我是{}'.format(self.getColor(),
                                                         self.getAge(), self.getWeight(),
                                                         self.getBrand()))

zy = Dog('黄色',10,5,'张岩')
zy.show()
