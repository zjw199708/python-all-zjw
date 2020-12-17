# a = [1,2,5,6,74,4,3,6]
# print(type(a))
# sum=0
# for i in range(len(a)):
#     sum+=a[i]
#     print(a[i])
# print('he',sum)


# max= a[0]
# index = -1
# for i in range(0,len(a)):
#     if a[i] >= max:
#         max = a[i]
#         index = i
#     sum+=a[i]
# print('a里的最大值为{}，对应角标为{},和{}'.format(max, index,sum))

shop = [
    ['Iphone',6000],
    ['Mac book',18888],
    ['小米10',6888],
    ['lenovo',4500],
    ['泡面',4.5]
]
print('欢迎来到张总超市购物广场'.center(70,'-')) # 开头提示
# 首先初始自己的金钱
while True:
    salary = input('请输入你的金钱：')
    if salary.isdigit():
        salary = int(salary)
        print('恭喜您的初始金钱为{}，祝您本次购物愉快'.format(salary))
        break
        pass
    else:
        print('穷逼买个锤子')
'''
    1. 输入商品编号
        1.1 输入不存在，重新进行输入
        1.2 您的余额是否充足，余额足够时，将需要买的当前商品添加到购物车
        1.3 余额不足 强行退出
    2. 输入Q或q，退出商城
    买的东西打印小票
'''
mycart =[]
sum = 0
change = 0
print(type(mycart))

while True:
    for index,value in enumerate(shop):
        print(index,value)
    choice = input('请输入你需要买的商品编号：')
    if choice.isdigit():
        num = int(input('请输入购买数量'))
        choice = int(choice)

        if choice < len(shop):
            if salary >= (num*shop[choice][1]): # 现有金额是否大于需要购买的金额
                mycart.append(shop[choice]) # 将商品名称和数量添加到购物车
                mycart.append(num)
                sum+=(num*shop[choice][1]) # 消费的金额
                change = salary - sum   # 余额
                print('\033[32;20;1m恭喜你，添加成功！您的余额还剩：', change, '\033[0m')
            else:
                print('\033[41;20;1m对不起，您的余额不足，穷逼充钱去吧！\033[0m')
        else:
            print('\033[42;20;1m瞎输啥呢？有这东西嘛你就在这儿输！二傻子\033[0m')
    elif choice == 'Q' or choice == 'q':
        print('欢迎下次再来！')
        break
    else:
        print('\033[42;20;1m瞎巴巴啥呢！重来！！！\033[0m')
print('==========走好不送==========')
print('收好您的小票，概不退换')
for i in mycart:
    print(i)
print('您共消费{}元,实付{}元，找零{}元'.format(sum,salary,change))

