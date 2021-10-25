# os模块
import os

# 创建目录
os.mkdir("testdir")

# 遍历目录
print(os.listdir("./"))

# 删除目录
os.removedirs("testdir")

# 获取当前路径
print(os.getcwd())  # 输出：D:\PycharmProjects\PyTest\testdemo

# 创建b/test.txt文件,并写入数据  b目录下的test.txt文件
print(os.path.exists("b"))
if not os.path.exists("b"):
    os.mkdir("b")
if not os.path.exists("b/test.txt"):
    f=open("b/test.txt","w")
    f.write("hello os using")
    f.close()


# time模块
import time
# 国外的时间格式
print(time.asctime()) # 输出：Mon Oct 18 19:32:24 2021
# 时间戳
print(time.time()) # 输出：1634556744.3626728
# 时间戳转成时间元组
print(time.localtime()) # 输出：time.struct_time(tm_year=2021, tm_mon=10, tm_mday=18, tm_hour=19, tm_min=32, tm_sec=24, tm_wday=0, tm_yday=291, tm_isdst=0)
# 将当前的时间戳转成带格式的时间
print(time.strftime("%Y-%m-%d %H-%M-%S",time.localtime())) # 输出：2021-10-18 19-37-05

# 获取两天前的世界
now_timestamp=time.time()
two_day_brfore=now_timestamp-60*60*24*2
time_tuple=time.localtime(two_day_brfore)
print(print(time.strftime("%Y-%m-%d %H-%M-%S", time_tuple))) # 输出：2021-10-16 19-42-18

# urllib库
import urllib.request

response:object=urllib.request.urlopen('http://www.baidu.com')
print(response.status)  # 输出：200
print(response.read()) # 输出：百度网页的html
print(response.headers) # 输出：headers头部信息

import math
# 返回大于等于参数x的最小整数
print(math.ceil(5.5))  # 输出：6

# 返回小于等于参数x的最大整数
print(math.floor(5.5)) # 输出：5

# 开平方根
print(math.sqrt(9)) # 输出：3.0

