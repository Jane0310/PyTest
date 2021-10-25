"""
列表的特性
（1）list.append(x)：在列表的末尾添加一个元素，相当于a[len(a):]=[x]
（2）list.insert(i,x)：在给定的位置插入一个元素。第一个参数是要插入的元素的索引，以a.insert(0,x)插入列表头部，a.insert(len(a),x)等同于a.append(x)
（3）list.remove(x)：移除列表中第一个值为x的元素。如果没有这样的元素，则抛出ValueError异常。
（4）list.pop([i])：删除列表中给定位置的元素并返回它。如果没有给定位置，a.pop()将会删除并返回列表中的最后一个元素。
（5）list.sort(key=None，reverse=False）：对列表中的元素进行排序（参数可用于自定义排序，解释请参见sorted()）
（6）list.reverse()：反转列表中的元素。
"""
# 添加
list_hogwarts=[1,2,3]
list_hogwarts.append("aaa")
print(list_hogwarts)  # 输出：[1, 2, 3, 'aaa']

# 插入
list_hogwarts.insert(1,"bbb")
print(list_hogwarts) # 输出：[1, 'bbb', 2, 3, 'aaa']

# 移除指定元素
list_hogwarts.remove(1)
print(list_hogwarts) # 输出：['bbb', 2, 3, 'aaa']

# 根据索引删除元素
list_hogwarts.pop(-1)
print(list_hogwarts) # 输出：['bbb', 2, 3]

# 排序
list_hogwarts2=[1,2,3,9,6,4,2]
list_hogwarts2.sort()
# 升序
print(list_hogwarts2) # 输出：[1, 2, 2, 3, 4, 6, 9]
# 降序
list_hogwarts2.sort(reverse=True)
print(list_hogwarts2) # 输出：[9, 6, 4, 3, 2, 2, 1]

# 反转
list_hogwarts2.reverse()
print(list_hogwarts2) # 输出：[9, 6, 4, 3, 2, 2, 1]

# 列表推导式
list_hogwarts3=[i**2 for i in range(1,4)]
print("list_hogwarts3",list_hogwarts3)  # 输出：list_hogwarts3 [1, 4, 9]

# 嵌套循环
list_square4=[]
for i in range(1,4):
    for j in range(1,4):
        list_square4.append(i*j)
print(list_square4)  # 输出：[1, 2, 3, 2, 4, 6, 3, 6, 9]