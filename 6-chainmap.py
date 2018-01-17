# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/17 0017 下午 3:56'

from collections import ChainMap

user_dict1 = {"a": "bobby1", "b": "bobby2"}
user_dict2 = {"c": "bobby2", "d": "bobby3"}
# chainmap将dict连接起来，可以直接进行for循环
# 当存在同一个key值，只会出现第一次的

new_dict = ChainMap(user_dict1, user_dict2)

# maps方法可以将chainmap类型变为列表,并且是指向性，可以直接修改原数据
print(new_dict.maps)
for key, value in new_dict.items():
    print(key, value)

print(new_dict["c"])