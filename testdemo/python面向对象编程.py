# 定义类
class Person:
    # 类变量
    name="nonase"

    # 类方法
    def get_name(self):
        return self.name

print(Person.name) # 输出：nonase
p=Person()
print(p.name)   # 输出：nonase
print(p.get_name()) # 输出：nonase

# 修改类变量
p.name="LiLi"
print(p.name)   # 输出：LiLi


class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def set_att(self,value):
        self.value=value

    def eat(self):
        print(f"name：{self.name},age：{self.age},gender:{self.gender},我在吃---")

    def drink(self):
        print(f"name：{self.name},age：{self.age},gender:{self.gender},我在喝---")

    def run(self):
        print(f"name：{self.name},age：{self.age},gender:{self.gender},我在跑---")


xiaoming=Person("xiaoming",10,"male")
xiaohong=Person("xiaohong",15,"female")
print(xiaoming.name) # 输出：xiaoming
xiaoming.run() # 输出：name：xiaoming,age：10,gender:male,我在跑---
xiaoming.set_att("fit")
print(xiaoming.value) # 输出：fit