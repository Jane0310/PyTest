# if分支
a = 1
if a == 0:
    print("a=0")
elif a == 1:
    print("a==1")
elif a == 2:
    print("a==2")
else:
    print("a不等于0,1,2")

# 分段函数求值
# 分支结构
x = -2
if x > 1:
    y = 3 * x - 5
else:
    if x >= -1:
        y = x + 2
    else:
        y = 5 * x + 3
print(y)

# 多重分支
if x > 1:
    y = 3 * x - 5
elif -1 <= x <= 1:
    y = x + 2
elif x <= -1:
    y = 5 * x + 3
print(y)


print("-------------------------------")

# for in 循环
# 1、计算1-100求和
sum=0
for i in range(1,101):
    # print(i)
    sum+=i
print(sum)

# 2、加入分支结构实现1-100之间的偶数求和
sum=0
for i in range(1,101):
    if i%2==0:
        sum+=i
print(sum)

# 3、使用python实现1-100之间的偶数求和
sum=0
for i in range(2,101,2):
    sum += i
print(sum)

print("-----------------------")
# while 循环
count=0
while count<=5:
    print(count)
    count+=1
else:
    print("count跳出循环的值为："+str(count))

# break continue的使用
for i in range(1,10):
    if i==5:
        break
    print(i)
print("##################")
for i in range(1,10):
    if i==5:
        continue
    print(i)

print("---------------------------")
# 猜数字游戏
import random
computer_number=random.randint(1,100)
while True:
    person_number=int(input("请输入一个数字\n"))
    if person_number>computer_number:
        print("小一点")
    elif person_number<computer_number:
        print("大一点")
    elif person_number==computer_number:
        print("猜对啦")
        break