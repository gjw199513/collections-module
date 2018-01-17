# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/17 0017 上午 9:44'


from collections import namedtuple


# 对于简单的数据，不需要对数据进行操作，可以不使用class，使用namedtuple
User = namedtuple("User", ["name", "age", "height", "edu"])

# 可以直接对其赋值
user = User(name="bobby", age=29, height=175, edu="master")

# 使用元组进行赋值
user_tuple = ("bobby", 29, 175)
user = User(*user_tuple, "master")

# 使用字典进行赋值
user_dict = {
    "name": "bobby",
    "age": 29,
    "height": 175
}
user = User(**user_dict, edu="master")

# 使用_make()插入值，只需传入可迭代对象（列表和元组和字典）即可，传入的值必须一致。
user_tuple = ("bobby", 29, 175, "master")
user = User._make(user_tuple)

# _asdict()将namedtuple对象转换为字典（OrderedDict）对象
print(user.age, user.name, user.height)

