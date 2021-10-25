a={1}
b=set()

print(type(a)) # 输出：<class 'set'>
print(type(b)) # 输出：<class 'set'>

num1={1,2,3}
num2={1,4,5}

# num1，num2集合取并集
print(num1.union(num2)) # 输出：{1, 2, 3, 4, 5}
#num1，num2集合取交集
print(num1.intersection(num2)) # 输出：{1}
# 取差集
print(num1.difference(num2)) # 输出：{2, 3}

c="aaaahshhsjsyybbxiiijhshyyhshhkkh"
# 去重集合
print(set(c))