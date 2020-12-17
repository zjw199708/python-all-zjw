'''
import pymysql
con = pymysql.connect(host ="localhost",user="root",password="",database="ltttest",charset="utf8")

# 通过连接来获取游标
cursor = con.cursor()
# 书写sql 语句
sql = "insert into person values('admin',45,500.63,'男')"
# 通过游标执行sql语句
s = cursor.execute(sql)
# 提交刚才执行的操作，提交给数据
con.commit()
# 关闭资源
cursor.close()
con.close()
'''
#
# import pymysql
# def mian():
#     a=input('请输入用户名')
#     b=int(input('请输入年龄'))
#     c=float(input('请输入薪资'))
#     d=input('请输入性别')
#     con = pymysql.connect(host='localhost',port=3306,
#                           user='root',password='',
#                           db='ltttest',charset='utf8')
#     with con.cursor() as cursor:
#         result=cursor.execute('insert into person values(%s,%s,%s,%s)',(a,b,c,d))
#     con.commit()
#     con.close()
# if __name__ == '__main__':
#     mian()

# 删除
# import pymysql
# def mian():
#     con = pymysql.connect(host='localhost',port=3306,
#                           user='root',password='',
#                           db='ltttest',charset='utf8')
#     with con.cursor() as cursor:
#         result=cursor.execute('delete from person where usernaem="张三"')
#     con.commit()
#     con.close()
# if __name__ == '__main__':
#     mian()

# import pymysql
# def mian():
#     user=input('请输入需要删除的用户名')
#     con = pymysql.connect(host='localhost',port=3306,
#                           user='root',password='',
#                           db='ltttest',charset='utf8')
#     with con.cursor() as cursor:
#         result=cursor.execute('delete from person where usernaem=%s',(user,))
#     con.commit()
#     con.close()
# if __name__ == '__main__':
#     mian()


# import pymysql
# def mian():
#     a=input('请输入需要修改的用户名')
#     b=int(input('请输入修改的年龄'))
#     c= float(input('请输入修改的薪资'))
#     d=input('请输入修改的性别')
#     con = pymysql.connect(host='localhost',port=3306,
#                           user='root',password='',
#                           db='ltttest',charset='utf8')
#     with con.cursor() as cursor:
#         result=cursor.execute('update person set age=%s,salary=%s,sex=%s where usernaem=%s',(b,c,d,a))
#     con.commit()
#     con.close()
# if __name__ == '__main__':
#     mian()

# import pymysql
#
#
# def mian():
#     user = input('请输入用户名')
#     con = pymysql.connect(host='localhost', port=3306,
#                           user='root', password='',
#                           db='ltttest', charset='utf8')
#     with con.cursor() as cursor:
#         result = cursor.execute('select age,salary,sex from person where usernaem=%s', (user))
#         one = cursor.fetchall()
#         print(one)
#     con.commit()
#     con.close()
#
#
# if __name__ == '__main__':
#     mian()

