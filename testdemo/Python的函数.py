# 函数的定义
def method(a):
    """
    函数方法说明
    :param a:
    :return:
    """
    print(a)
    return a


# 函数的调用
method("aaa")


# 默认参数的定义
def method(a=0):
    print(a)


method()


# 关键字参数
def method(a, b):
    print(a)
    print(b)


method(a=1, b=2)
method(b=1, a=2)


# 字典传参
def method(**a):
    print(a.keys())


method(a=1, b=2, c=3)


# 元祖传参
def method(*a):
    print(a[0])
    print(a[1])
    print(a[2])


method(1, 2, 3)


# 解包模式
def method(a, b, c):
    print("解包模式-----------")
    print(a)
    print(b)
    print(c)


dic1 = {"a": 10, "b": 12, "c": 13}
method(**dic1)

# lambda表达式
y = lambda x, y, z: x + y + z
print(y(2, 3, 4))
