import random
num = random.randint(0,2000)
a = 0
while True:
    guess = int(input('请输入一个数字'))
    a+=1
    if guess == num:
        print('猜对啦，本次数字为{},共猜了{}次'.format(guess,a))
        break
    elif guess > num:
        print('辣鸡，猜大了')
    else:
        print('食屎啦，猜小了')





