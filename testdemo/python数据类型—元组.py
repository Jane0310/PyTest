# 元组的定义
tuple_hogwarts=(1,2,3)
tuple_hogwarts2=1,2,3

print("tuple_hogwarts",tuple_hogwarts) # 输出：tuple_hogwarts (1, 2, 3)
print(type(tuple_hogwarts)) # 输出：<class 'tuple'>

print("tuple_hogwarts2",tuple_hogwarts2) # 输出：tuple_hogwarts2 (1, 2, 3)
print((type(tuple_hogwarts2))) # 输出：<class 'tuple'>

# 元组的不可变特性
a=(1,2,3)
tuple_hogwarts3=(4,5,a)
print(tuple_hogwarts3) # 输出：(4, 5, (1, 2, 3))


b=(1,2,3,"a","a")
# 获取内容出现的个数
print(b.count("a"))  # 输出：2
# 打印字母a出现的索引值，若有重复，则打印第一次出现的索引值
print(b.index("a")) #输出：3

