# db = {}
# f = open('人员信息.txt','r+',encoding='utf-8')
# date = f.readlines()
# for i in date:
#     print(i)
#     line = i.split(',')
#     db[line[0]] = line[1].replace("\n", "")
# f.close()
# name = input('请输入用户名：')
# password = input('请输入密码')
# if name in db:
#     if password == db[name]:
#         print('登录成功')
#     else:
#         print('密码输入错误')
# else:
#     print('该用户不存在')


# f = open('scores.txt','r+',encoding='utf-8')
# data = f.readlines()
# for i in data:
#     sum = 0
#     line = i.split()
#     print(line)
#     line[1:] =map(int,line[1:])
#     print(line[1:])
#     for j in line[1:]:
#         sum+=j
#     print(sum)
# f.close()


# f = open('baidu_x_system.log', 'r+', encoding='utf-8')
# date = f.readlines()
# a = []
# for i in date:
#     line = i.split('- -')
#     a.append(line[0])
# print(a)
# for index, ch in enumerate(a):
#     if ch in a[:index]:
#         continue
#     print(ch, '出现了', a.count(ch))
# f.close()

# f = open("baidu_x_system.log","r+",encoding="utf-8")
# dic = {} #  {ip:次数}
# lines = f.readlines()
#
# for line in lines:
#     ip = line.split(" ")[0]
#     if ip in dic:
#         dic[ip] =  dic[ip] + 1
#     else:
#         dic[ip] = 1
#
# print(dic)
# a = open('text.txt','w',encoding='utf-8')
# for key in dic:
#     a.write('{id}:{count}\n'.format(id=key,count=dic[key]))
# a.close()

f = open("scores.txt","r+",encoding="utf-8")
dic = {}# 姓名:总分

lines = f.readlines()# ["罗恩 23 35 44" , "哈利 60 77 68 88 90"...]

for line in lines:
    li = line.replace("\n","").split(" ") # ["罗恩","23","35","44"]
    name = li[0] # "罗恩"
    scores = li[1:] # ["23","35","44"]
    dic[name] = sum([int(i) for i in scores])# [23 35 44]  lambda   兰不大表达式：效率更高

print(dic)

a = open('text1.txt','w+',encoding='utf-8')
for key in dic:
    a.write('{name}:{count}\n'.format(name=key,count=dic[key]))
a.close()