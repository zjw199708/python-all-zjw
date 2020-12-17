# import random
# num =int(random.random()*100+50)
# print(num)

# a,b,c=map(int,input('请输入三边长').split())
# if a+b>c and a+c>b and b+c>a:
#     if a == b and a == c:
#         print('等边三角形')
#         pass
#     elif a==b or a==c or b==c:
#         print('等腰三角形')
#         pass
#     else:
#         print('普通三角形')
# else:
#     print('瞎巴巴啥')

# A=56
# B=78
# A=A+B
# B=A-B
# A=A-B
# print('A=',A)
# print('B=',B)


# a = 0
# while a <3:
#     password=int(input('请输入密码'))
#     if password == 8888:
#         print('密码输入正确')
#         pass
#     else:
#         print('密码输入错误')
#         pass
#     a+=1
# else:
#     print('三次输入错误，账户锁定')


# i=1
# while i<=7:
#     j = 1
#     while j <= 7-i:
#         print(' ', end='')
#         j += 1
#     k = 1
#     while k <=i:
#         print('* ',end='')
#         k += 1
#     print()
#     i+=1

# i=1
# while i<=7:
#     j = 1
#     while j <= 7-i:
#         print(' ', end='')
#         j += 1
#     k = 1
#     while k <=i*2-1:
#         print('*',end='')
#         k += 1
#     print()
#     i+=1


num = 9
i = 9
while i <= num and i>0:
    j = 1
    while j <= i:
        print(j,"x",i,"=",(i*j),end="\t")
        j+=1
    print()
    i = i - 1

# height,up,down=map(int,input('请输入高度，白天爬行，夜晚掉落').split())
# i = 1
# sum=0
# while i>0:
#     sum=sum+up
#     if sum >= height:
#         print('老子出来了！')
#         break
#         pass
#     i+=1
#     sum=sum-down
#     pass
# print(i)




