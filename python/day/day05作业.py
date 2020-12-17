
sum = 0
# for i in a:
#     if i%5 == 0:
#         sum+=i
# print(sum)
#
# a = sorted(a)
# print(a)
#
# a = sorted(a,reverse=True)
# print(a)
# a = [1,5,21,8,15,9,30,24]
# for i in range(len(a)-1):
#     for j in range(0,len(a)-1-i):
#         if a[j] > a[j+1]:
#             a[j],a[j+1] = a[j+1],a[j]
#     print(a)
# 冒泡排序
# for i in range(len(a)-1):
#     for j in range(0,len(a)-1-i):
#         if a[j] < a[j+1]:
#             a[j],a[j+1] = a[j+1],a[j]
# print(a)
# 选择排序

number = [8,7,9,4]
for i in range(len(number)):
    for j in range(i+1,len(number)):
        if number[i]>number[j]:
            number[i],number[j]=number[j],number[i]
    print(number)

# li = list(str)
# for i in range(0,len(li)):
#     count = 0
#     flag = True
#     for k in range(0,i):
#         if li[k] == li[i]:
#             flag = False
#             break
#     if flag == False:
#         continue
#     for j in range(0,len(li)):
#         if li[i] == li[j]:
#             count+=1
#     print(li[i],'出现了',count,'次')
'''str = 'this is a da shuai bi, that is a chou dong xi'
for index,ch in enumerate(str):  # 枚举每一个字符出现的角标+字符
    if ch in str[:index]:    # 使用切片判断之前是否出现过
        continue
    print(ch,'出现了',str.count(ch)) # 通过count（）方法统计出现次数
'''
# def sum(a,b) :
#     c = a + b
#     return c
# s = sum(1,2)
# print(s)
# s= sum(66,99)
# print(s)
