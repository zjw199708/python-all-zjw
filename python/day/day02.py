str='12345'
print(str.isdigit())
int(str)
print(str)


# num1=int(input('请输入第一个数'))
# num2=int(input('请输入第二个数'))
# num3=int(input('请输入第三个数'))
# num4=int(input('请输入第四个数'))
# num5=int(input('请输入第五个数'))
# num6=int(input('请输入第六个数'))
# num7=int(input('请输入第七个数'))
# num8=int(input('请输入第八个数'))
# num9=int(input('请输入第九个数'))
# num10=int(input('请输入第十个数'))
num1,num2,num3,num4,num5,num6,num7,num8,num9,num10=map(int,input('请输入10个数用空格隔开').split())
print(num1+num2+num3+num4+num5+num6+num7+num8+num9+num10)

name=input('请输入您的姓名')
numberID=input('请输入您的身份证号')
age=int(input('请输入您的年龄'))
sex=input('请输入您的性别')
height=input('请输入您的身高')
weight=input('请输入您的体重')
if age >= 18 and age < 100:
    print('可以看电影去了')
    pass
elif age < 18 and age >=0:
    print('小屁孩看什么看')
    pass
else:
    print('你是外星人啊，瞎输啥？？？')
    pass


stu1=45
stu2=23
print(stu1+stu2)

nu1=45
nu2=nu1
print(nu2)

