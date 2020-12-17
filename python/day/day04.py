'''
用户从键盘输入整形数值，若输入的是1，则继续让用户输入数值n并打印n*n的乘法表。
若用户输入的是编号2，则继续让用户输入数值m并打印m层等腰三角形吗。若用户输入除了1,2,
以外的数值请优化程序并提示输入有误和重新进行输入。
'''

# while True:
#     i = int(input('请输入1或2'))
#     if i == 1:
#         multiplication = int(input('请输入乘法表层数'))
#         for a in range(0, multiplication + 1):
#             for b in range(1, a + 1):
#                 print(a, '*', b, '=', (b * a), end='\t')
#             print()
#         break
#     elif i == 2:
#         triangle = int(input('请输入三角形层数'))
#         c = 1
#         while c <= triangle:
#             d = 1
#             while d <= (triangle - c):
#                 print(' ', end='')
#                 d += 1
#                 pass
#             e = 1
#             while e <= c:
#                 print('* ', end='')
#                 e += 1
#             print()
#             c += 1
#         break
#     else:
#         print('瞎巴巴啥呢!重新来')

'''用循环来实现20以内的数的阶乘。（1! +2!+3!+…..+20!）'''
# ride = 1
# for i in range(1,21):
#     ride=(ride*i)
#     print(i,'!','=',ride)




'''从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数。'''
# a,b,c,d,e,f,g,h,i,j=map(int,input('请输入十个数').split())
# he=a+b+c+d+e+f+g+h+i+j
# average=he/10
# sum=0

# print('和为{}，平均数为{}，最大值为{}'.format(he,average,sum))
# max = 0
# sum = 1
# for i in range(10):
#     a= int(input('请输入数'))
#     if a>max :
#         max = a
#         sum = sum +a
#         pass
# print('最大值',max)


# num =int(input('请输入数字'))
# while num != 0:
#     print(num%10)
#     num=num//10

# ride = 1
# sum=0
# for i in range(1,21):
#     ride=(ride*i)
#     sum+=ride
# print(sum)

# author:jason
shop = [
    ["Iphone",6000],
    ["Mac computer",12000],
    ["小米 watch",500],
    ["lenovo pc",4500],
    ["辣条",2.5],
    ["泡椒鸡爪",13],
    ["老干妈",10]
]
# 二维列表，一维列表又套个一维列表f
print("欢迎来到Jason超市购物广场".center(70,"-"))

# 1.先初始化自己的金钱
while True:
    salary = input("请输入您的初始金钱：")
    if salary.isdigit():# 判断输入的字符串是否能看成数字
        salary =  int(salary)
        print("恭喜您的您的初始金钱为",salary,"，祝您本次购物愉快！")
        break
    else:
        print("请重新输入您的初始余额！")

'''
    1. 输入商品编号
        1.1 输入不存在，打回去重新输入
        1.2 您的余额是否充足。买东西，需要将当前商品添加我的购物车里，余额还要减去那么多钱。
        1.3 若您的余额不足，强行退出。
    2.输入Q,q。退出商城。
    买的东西打一下小票。
'''
# 1.定义一个我的购物车
mycart = []

while True:
    # 展示所有商品
    for index, value in enumerate(shop):
        print(index, "  ", value)
    choice = input("请输入您要买的商品编号：")
    if choice.isdigit():
        choice = int(choice)
        if choice < len(shop):
            if salary >= shop[choice][1]:
                mycart.append(shop[choice]) # 添加到我的购物车
                salary -=  shop[choice][1]
                print("\033[32;20;1m恭喜你，添加成功！您的余额还剩：",salary,"\033[0m")
            else:
                print("\033[41;20;1m对不起，您的月不足，穷鬼！请退出!\033[0m")
        else:
            print("\033[42;20;1m您输入的商品编号它不存在！请重新输入\033[0m")
    elif choice  == 'q' or choice == 'Q':
        print("欢迎下次光临！！！")
        break
    else:
        print("\033[42;20;1m您的输入不合法，请重新输入！！！！\033[0m")
print("-------------------Bye!-------------------")


# 2.打印我的小票
for i in mycart:
    print(i)
print("您的余额为：",salary)
















