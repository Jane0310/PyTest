import baidu
from baidu import name_is_a_very_long_name,add,index

# 使用import baidu之后的引用
print(baidu.name_is_a_very_long_name)
print(baidu.add(1,5))
i=baidu.index()
print(i.sub(1,6))

print("-----------------------------------")
# 使用from baidu import name_is_a_very_long_name,add,index之后的引用
print(name_is_a_very_long_name)
print(add(1,5))
i=index()
print(i.sub(1,6))