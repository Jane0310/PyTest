# 定义
dict_1={"a":1,"b":2}
dic_2=dict(a=1,b=2)

print("dict_1",dict_1) # 输出：dict_1 {'a': 1, 'b': 2}
print(type(dict_1)) # 输出：<class 'dict'>
print("dic_2",dic_2) #输出：dic_2 {'a': 1, 'b': 2}

# 输出键
print(dict_1.keys()) # 输出：dict_keys(['a', 'b'])
# 输出值
print(dict_1.values()) # 输出：dict_values([1, 2])
# 删除指定的key
dict_1.pop("a")
print(dict_1)  # 输出：{'b': 2}

# 删除随机的键值对
print(dic_2.popitem()) # 输出：('b', 2)
# 删除之后输出
print(dic_2) # 输出：{'a': 1}