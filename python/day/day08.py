# # 1. 打开文件，并获取文件句柄
# f=open('a.txt','w+',encoding='utf-8')
# # 2. 写入数据
# f.write('万能的测试开发''\n')
# f.write('床前明月光')
# # 3. 关闭资源
# f.close()

#
# f = open('123.jpg', 'rb')  # 读取
# w = open('D:\python\美铝啊.jpg', 'wb')  # 写入
# # 将读取的数据存放到一个容器内
# date = f.read()
#
# w.write(date)
#
# f.close()
# w.close()
# 将所有数据提取，存储到字典里（字典：缓冲区，便于快速修改）
db ={}
f = open('a.txt','r+',encoding='utf-8') # 读取 a.txt文件
date = f.readlines() # 存储到date里 ['张三：123456'，'李四：admin']
print(date)
for i in date:
    line = i.split(':') # 将上侧列表拆分开 ['张三'，'123456']
    db[line[0]] = line[1].replace('\n','') # 将列表后的\n删除
    print(date)
name = input('请输入用户名')
password = input('请输入密码')
'''
 1. 先判断是否存在该用户
    若存在，继续判断密码是否正确
       密码正确，登录成功
       密码错误，登录失败
    若不存在 ，提示该用户不存在

'''
if name in db:
    if password == db[name]:
        print('登录成功')
    else:
        print('密码错误')
else:
    print('该用户不存在')
    
