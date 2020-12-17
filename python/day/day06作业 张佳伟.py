# list1 = [1,2,3,4,5,6,7,8,9]
# print(list1[::-1])
#
# list2 = [1, 4, 7, 5, 82, 1, 3, 4, 5, 9, 7, 6, 1, 10]
# for index, num in enumerate(list2):
#     if num in list2[:index]:
#         continue
#     print(num, '出现了', list2.count(num))

# 姓名  年龄  性别  编号  任职公司 薪资 部门编号
# names = [
#     ["何登勇", "56", "男", "106", "IBM", 500, "50"],
#     ["曹东雪", "19", "女", "230", "微软", 501, "60"],
#     ["刘营营", "19", "女", "210", "Oracle", 600, "60"],
#     ["李汉聪", "45", "男", "230", "Tencent", 700, "10"]
# ]
#  统计所有人的平均薪资
# sum = 0
# for i in range(len(names)):
#     sum += names[i][5]
# print(sum/4)

# 统计所有人的平均年龄
# sum = 0
# sun = 0
# for i in range(len(names)):
#     sum = int(names[i][1])
#     sun += sum
# print(sun / len(names))

# 公司新来一个员工，张佳伟，45，男，220，alibaba，500,30，添加到列表中
# names.append(['张佳伟','45','男','220','alibab',500,'30'])
# print(names)

# 统计公司男女人数
# man = 0
# woman = 0
# for i in range(len(names)):
#     if '男' in names[i]:
#         man+=1
#     if '女' in names[i]:
#         woman+=1
# print('公司男人有{}人，女人有{}人'.format(man,woman))

# 每个部门的人数
# list2 = [1, 4, 7, 5, 82, 1, 3, 4, 5, 9, 7, 6, 1, 10]
# d = {}
# for i in list2:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1
# print(d)


# def showinfo(name, age, *args):
#     print(name, age)
#     print(args)
#     print(type(args))
#     for i in args:
#         print(i)
#
#
# showinfo('张张章', 89, '男', 185, '456215621')


# 求和 不计数量的求和

# def sum(*args):
#     sun = 0
#     for i in args:
#         sun += i
#     print(sun)
#
#
# sum(5,9,10,1,10,20,30)

# 用方法打印1-100
def num():
    i = 0
    
    print(i)

