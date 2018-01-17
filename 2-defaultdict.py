# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/17 0017 上午 11:30'

from collections import defaultdict

user_dict = {}
users = ["bobby1", "bobby2", "bobby3", "bobby1", "bobby2", "bobby2"]
# 对users中的用户名进行统计放入字典中输入
# for user in users:
#     # 在对应的key时，字典无法运算，需要通过赋值来对字典的key和value进行初始化
#     if user not in user_dict:
#         user_dict[user] = 1
#     else:
#         user_dict[user] += 1

# 使用setdefault进行初始化赋值，实现上述代码同样的效果
# 该方法更加高效，因为少做了一次查询操作
# for user in users:
#     user_dict.setdefault(user, 0)
#     user_dict[user] += 1

# print(user_dict)


# 使用defaultdict可以完成上述操作
default_dict = defaultdict(int)

for user in users:
    default_dict[user] += 1


# 使用defaultdict创建一个复杂默认的字典
def gen_default():
    return {
        "name": "",
        "nums": 0
    }
default_dict = defaultdict(gen_default)
default_dict["group1"]
print(default_dict)

