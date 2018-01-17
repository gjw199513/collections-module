# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/17 0017 下午 3:44'

from collections import OrderedDict

# ordereddict可以按照添加的顺序存储，在python3中dict默认有序
user_dict = OrderedDict()
user_dict["b"] = "bobby2"
user_dict["a"] = "bobby1"
user_dict["c"] = "bobby3"

# pop可以将最后一个元素删除，必须传递删除的key值
# print(user_dict.pop("a"))

# popitem()直接删除最后一个元素
# print(user_dict.popitem())

# move_to_end可以将一个元素直接移动到最后
user_dict.move_to_end("a")
print(user_dict)


