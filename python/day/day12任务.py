# class Calc:
#     def addition(*num):
#         sum = 0
#         for i in num:
#             sum += i
#         print(sum)
#
#     def substruction(*num):
#         sum = num[0]
#         for i in num[1:]:
#             sum -= i
#         print(sum)
#
#     def multiplication(*num):
#         sum = num[0]
#         for i in num[1:]:
#             sum *= i
#         print(sum)
#
#     def division(num1, num2):
#         sum = num1 / num2
#         print(sum)
#
#
# class Test(Calc):
#     pass
#
#
# calc = Test
# calc.addition(1, 2, 3, 5, 6)
# calc.substruction(10, 1, 2, 3)
# calc.multiplication(2, 3, 6)
# calc.division(10, 5)


class Old:
    __brand = None

    def __init__(self, brand):
        self.__brand = brand

    def setBrand(self, brand):
        self.__brand = brand

    def getBrand(self):
        return self.__brand

    def call(self, name):
        print('正在给{}打电话'.format(name))


class New(Old):
    def __init__(self, brand):
        super().__init__(brand)

    def callnew(self, name):
        print('语音拨号中')
        super().call(name)

    def info(self):
        print('{}的手机很好用'.format(self.getBrand()))


old = Old('华为')
old.call('name')
new = New('小米')
new.callnew('张总')
new.info()


# class Cook:
#     __age = None
#     __name = None
#
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     def setName(self, name):
#         self.__name = name
#
#     def getName(self):
#         return self.__name
#
#     def setAge(self, age):
#         self.__age = age
#
#     def getAge(self):
#         return self.__age
#
#     def rice(self):
#         print('{}正在蒸饭'.format(self.__name))
#
#
# class Cook1(Cook):
#     def __init__(self, name, age):
#         super().__init__(name, age)
#
#     def vegetables(self):
#         print('{}正在炒菜'.format(self.getName()))
#
#
# class Cook2(Cook1):
#     def __init__(self, name, age):
#         super().__init__(name, age)
#
#     def rice1(self):
#         print('蒸饭')
#
#     def vegetables1(self):
#         print('炒菜')
#
#
# class Cook3(Cook2):
#     def __init__(self, name, age):
#         super().__init__(name, age)
#
#     def show(self):
#         print('这个厨师叫{}今年{}岁'.format(self.getName(), self.getAge()))
#
# cook3 = Cook3('张岩',150)
# cook3.setAge(50)
# cook3.setName('构师')
# cook3.show()
# cook3.rice()


# class Person:
#     __name = None
#     __sex = None
#     __age = None
#
#     def __init__(self, name, age, sex):
#         self.__name = name
#         self.__sex = sex
#         self.__age = age
#
#     def setName(self, name):
#         self.__name = name
#
#     def getName(self):
#         return self.__name
#
#     def setSex(self, sex):
#         self.__sex = sex
#
#     def getSex(self):
#         return self.__sex
#
#     def setAge(self, age):
#         self.__age = age
#
#     def getAge(self):
#         return self.__age
#
#     def show(self):
#         print('这个人的姓名是{}，性别为{}，年龄{}岁'.format(self.getName(), self.getSex(), self.getAge()))
#
#
# class Worker(Person):
#     def __init__(self, name, age, sex):
#         super().__init__(name, age, sex)
#
#     def work(self):
#         print('{}在干活'.format(self.getName()))
#
#
# class Student(Person):
#     def __init__(self, name, age, sex):
#         super().__init__(name, age, sex)
#
#     def study(self):
#         print('{}正在学习，今年{}岁，是个{}的'.format(self.getName(), self.getAge(), self.getSex()))
#
#     def sing(self):
#         print('{}正在唱歌，今年{}岁，是个{}的'.format(self.getName(), self.getAge(), self.getSex()))
#
# zy = Student('张岩',88,'男')
# zy.sing()
# zy.study()