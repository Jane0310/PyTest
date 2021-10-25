import yaml

# load加载  将yaml文件的内容输出成不同格式的数据
# 1、输出一个列表
print(yaml.load("""
- Hesperiidae
- Papilionidae
- Apatelodidae
- Epipleidae
""",Loader=yaml.FullLoader))  # 输出：['Hesperiidae', 'Papilionidae', 'Apatelodidae', 'Epipleidae']

# 2、输出一个字典
print(yaml.load("""
a : 1
""", Loader=yaml.FullLoader)) # 输出：{'a': 1}

# 3、直接调用外部文件 列表形式：
"""
-
  - Hesperiidae
  - Papilionidae
-
  - Apatelodidae
  - Epipleidae
- a: 1
"""
print(yaml.load(open("demo.yml"),Loader=yaml.FullLoader))
# 输出：[['Hesperiidae', 'Papilionidae'], ['Apatelodidae', 'Epipleidae'], {'a': 1}]

# 4、直接调用外部文件 字典形式：
"""
a: 1
b: 2
c: 3
"""
print(yaml.load(open("demo2.yml"),Loader=yaml.FullLoader))
# 输出：{'a': 1, 'b': 2, 'c': 3}


# 5、直接调用外部文件 字典嵌套列表形式：
"""
a:
  - 1
  - 2
"""
print(yaml.load(open("demo3.yml"),Loader=yaml.FullLoader))

print("-----------------------dump的使用--------------")
# dump的使用  将不同格式的数据解析成yaml格式的数据
print(yaml.dump({'a': [1, 2]}))
"""
输出：
a:
- 1
- 2
"""

# 将数据写入yaml格式的文件中
with open("demo4.yml","w") as f:
    yaml.dump(data={'a': [1, 2]},stream=f)