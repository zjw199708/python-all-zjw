#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 我的163授权码：OKIADSGIYSTENULF，qq授权码:pxwctgopudmbdhif
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

sender = '2431320433@qq.com'
receivers = ['1468359547@qq.com',
             '13552648187@163.com',
             '1402162946@qq.com',
             '2398710377@qq.com',
             '1020397800@qq.com',
             '2867242015@qq.com',
             '2371770485@qq.com',
             "1877762890@qq.com",
             '2075518412@qq.com',
             '852761403@qq.com',
             '2863946574@qq.com',
             '1010454316@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
mail_host = 'smtp.qq.com'
password = 'pxwctgopudmbdhif'
tester = '贾生'
# 创建一个带附件的实例
message = MIMEMultipart()
message['From'] = '2431320433@qq.com'
message['To'] = Header("Jason的邮件", 'utf-8')
subject = '第一轮银行的单元测试报告 -- [' + tester + ']'
message['Subject'] = Header(subject, 'utf-8')

# 邮件正文内容
message.attach(MIMEText('详情请见附件消息！', 'plain', 'utf-8'))

# 构造附件1，传送当前目录下的 test.txt 文件
f = open('计算器测试报告.html', 'r+',encoding="utf-8").read() # 先读取报告文件
att1 = MIMEText(f, 'base64', 'utf-8')  # 添加到附件里
att1["Content-Type"] = 'application/octet-stream' # 添加属性头
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="bank_reporting.html"'
message.attach(att1)

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host,25)
    smtpObj.login(sender,password)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException as e:
    print("Error: 无法发送邮件",e)