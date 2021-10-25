# 字面量插值
# 字符串
print("we are the {} and {}".format('Tom','Jerry')) # 输出：we are the Tom and Jerry

# 列表
listdata=["Time","Jone"]
print("we are the {0} and {1}".format(*listdata)) # 输出：we are the Time and Jone

# 字典
dictdata={"name":"LiLi","age":30}
print("my name is {name},age is {age}".format(**dictdata)) # 输出：my name id LiLi,age is 30

name="ERIC"
print(f'my name is {name}') # 输出：my name is ERIC
print(f'my name is {name.lower()}') # 输出：my name is eric

print("----------------------------------------")
# 文件读取
f=open('D:\PycharmProjects\PyTest/testdemo/txtfile.txt','rt')
print(f.read())
# 关闭文件
f.close()

# 使用如下的格式可以不调用f.close()方法，能够自动回收文件
with open('D:\PycharmProjects\PyTest/testdemo/txtfile.txt','rt') as f:
    print(f.readlines())

print("-----------------------------")
# json格式化
import json
info=[
    {
        "name":"Tom",
        "gener":"male",
        "other": None
    },
    {
        "name":"Jack",
        "gener":"male",
        "other": None

    }
]
# dumps：将python中的字典 转换为 字符串
# sort_keys: 以key值进行排序
# indent：以缩进的方式进行文本的输出 4个格的缩进
data=json.dumps(info,sort_keys=True,indent=4)
print("dumps方法的使用----------------------")
print(data)
print(type(data)) # 输出：<class 'str'>

# dump：把数据类型转换成字符串并存储在文件中
print("dump方法的使用----------------------")
print("写入json文件")
json.dump(info,open("D:\PycharmProjects\PyTest/testdemo/txtfile.txt","w"))

# load：把文件打开将字符串转换成json
jsObj=json.load(open("D:\PycharmProjects\PyTest/testdemo/txtfile.txt","r"))
print("load方法的使用----------------------")
print(jsObj) # 输出：[{'name': 'Tom', 'gener': 'male', 'other': None}, {'name': 'Jack', 'gener': 'male', 'other': None}]
print(type(jsObj)) # 输出：<class 'list'>
print(jsObj[0]["name"]) # 输出：Tom