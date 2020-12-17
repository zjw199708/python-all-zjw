'''
class bear:
    __brand = None
    __price = None
    def __init__(self,brand,price):
        self.__brand=brand
        self.__price=price
    def setBrand(self, brand):
        self.__brand = brand

    def getBrand(self):
        return self.__brand

    def setPrice(self, price):
        self.__price = price

    def getPrice(self):
        return self.__price

    def open(self):
        print('空调开机了')

    def close(self, time):
        print('空调将在{}分钟后关机'.format(time))

geli  = bear('格力',2999)

print('空调：{}，价格：{}'.format(geli.getBrand(),geli.getPrice()))

geli.open()
geli.close(20)

class Student:
    __name = None
    __age = None

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setAge(self, age):
        self.__age = age

    def getAge(self):
        return self.__age

    def introduction(self):
        print('我叫{}，今年{}岁'.format(self.__name,self.__age))

    def compare(self,name,age):
        if age > self.__age:
            a = age - self.__age
            print('{}比{}大了{}岁'.format(name,self.__name,a))
        elif age < self.__age:
            a = self.__age - age
            print('{}比{}小了{}岁'.format(name, self.__name, a))
        else:
            print('{}和{}一样大'.format(name,self.__name))
zy = Student('张岩',99)
zy.introduction()
zy.compare('zz',90)
'''
'''
class People:
    __name = None
    __sex = None
    __age = None
    __money = None
    __brand = None
    __battery = None
    __size = None
    __bide = None
    __integral = None

    def __init__(self, name, sex, age, money, brand, battery, size, bide, intergal):
        self.__name = name
        self.__age = age
        self.__sex = sex
        self.__money = money
        self.__brand = brand
        self.__battery = battery
        self.__size = size
        self.__bide = bide
        self.__integral = intergal

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setSex(self, sex):
        self.__sex = sex

    def getSex(self):
        return self.__sex

    def setMoney(self, money):
        self.__money = money

    def getMoney(self):
        return self.__money

    def setBrand(self, brand):
        self.__brand = brand

    def getBrand(self):
        return self.__brand

    def setBattery(self, battery):
        self.__battery = battery

    def getBattery(self):
        return self.__battery

    def setSize(self, size):
        self.__size = size

    def getSize(self):
        return self.__size

    def setBide(self, bide):
        self.__bide = bide

    def getBide(self):
        return self.__bide

    def setIntegral(self, intergral):
        self.__integral = intergral

    def getIntegral(self):
        return self.__integral

    def message(self, message):
        print('发送成功，内容为{}'.format(message))

    def call(self, phone, time):
        phone = str(phone)
        if len(phone) == 0 or self.__money < 1:
            print('请检查拨打号码是否为空，以及您的余额')
        elif time < 10 and time > 0:
            self.__money -= 1 * time
            self.__integral += 15 * time
            print('您的余额为{}，积分为{}'.format(self.__money, self.__integral))
        elif time >= 10 and time <= 20:
            self.__money -= 0.8 * time
            self.__integral += 39 * time
            print('您的余额为{}，积分为{}'.format(self.__money, self.__integral))
        else:
            self.__money -= 0.65 * time
            self.__integral += 48 * time
            print('您的余额为{}，积分为{}'.format(self.__money, self.__integral))
            pass
'''

# zy = People('张岩', '男', '23', 0.1, '华为', '2800mA', '12.8', '8h', 200)
# zy.message('你好傻逼')
# zy.call(123456,10)

'''
class Student:
    __number = None
    __name = None
    __age = None
    __sex = None
    __height = None
    __weight = None
    __score = None
    __address = None
    __phone = None

    def __init__(self, number, name, age, sex, height, weight, score, address, phone):
        self.__number = number
        self.__name = name
        self.__age = age
        self.__sex = sex
        self.__height = height
        self.__weight = weight
        self.__score = score
        self.__address = address
        self.__phone = phone

    def setNumber(self, number):
        self.__number = number

    def getNumber(self):
        return self.__number

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setAge(self, age):
        self.__age = age

    def getAge(self):
        return self.__age

    def setSex(self, sex):
        self.__sex = sex

    def getSex(self):
        return self.__sex

    def setHeight(self, height):
        self.__height = height

    def getHeight(self):
        return self.__height

    def setWeight(self, weight):
        self.__weight = weight

    def getWeight(self):
        return self.__weight

    def setScore(self, score):
        self.__score = score

    def getScore(self):
        return self.__score

    def setAddress(self, address):
        self.__address = address

    def getAddress(self):
        return self.__address

    def setPhone(self, phone):
        self.__phone = phone

    def getPhone(self):
        return self.__phone

    def learn(self, time):
        print('{}学习了{}小时'.format(self.__name, time))

    def play(self, play):
        print('{}玩了{}游戏'.format(self.__name, play))

    def sun(self, *number):
        sum = 0
        for num in number:
            sum += num
        print('所求数的何为{}'.format(sum))


zy = Student(20, '张岩', 20, '男', 120, 120, 8, '内蒙', 12138)

zy.sun(1, 2, 3, 4)
'''


# class Car:
#     def __init__(self, type, wheel, color, weight, fat):
#         self.__type = type
#         self.__wheel = wheel
#         self.__color = color
#         self.__weight = weight
#         self.__fat = fat
#
#     def cross(self, type):
#         print('{}可以进行越野'.format(self.__type))
#
#     def overtake(self, type):
#         print('{}可以进行赛车'.format(self.__type))
#
#     def info(self):
#         print('{}有{}个轮子，车身颜色为{}，车重{}，能存{}油'.format(self.__type,
#                                                    self.__wheel, self.__color
#                                                    , self.__weight, self.__fat))
#
#
# fll = Car('法拉利', 4, '宝石蓝', '58kg', '40L')
# fll.info()
# fll.cross(fll)
# fll.overtake(fll)
#
#
# class Monkey:
#     def __init__(self, sort, sex, color, weight):
#         self.__sort = sort
#         self.__sex = sex
#         self.__color = color
#         self.__weight = weight
#
#     def fire(self, material):
#         print('{}可以用{}来造火'.format(self.__sort, material))
#
#     def learn(self, *subject):
#         for i in subject:
#             print('{}可以学习{}'.format(self.__sort, i))
#
#     def info(self):
#         print('这只猴子是：{}，性别：{}，颜色：{}，重量{}'.format(self.__sort, self.__sex,
#                                                  self.__color, self.__weight))
#
#
# zy = Monkey('张岩', '男', '黑', '120kg')
# zy.learn('吃饭', '喝水', '打人')
# zy.fire('木棒')
# zy.info()

