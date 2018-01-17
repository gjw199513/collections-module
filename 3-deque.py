# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/17 0017 下午 3:01'

# deque GTL是线程安全的，list不是线程安全的

from collections import deque

# deque可以初始化可迭代对象（list、tuple、dict）
user_deque = deque(["bobby1", "bobby2", "bobby3"])
# 在列表头加入数据
# user_deque.appendleft("bobby8")

# copy()是浅拷贝，当deque里面的数据是可变对象，则会同时改变二者
user_deque2 = user_deque.copy()
print(id(user_deque), id(user_deque2))
user_deque2[1] = "bobby3"

# extend是对deque对象连接，该方法不会返回新值，只会对原来的对象扩容
user_deque2.extend(user_deque)

# insert可以在指定位置插入元素
user_deque.insert(0, "bobby12")
print(user_deque, user_deque2)
print(user_deque)
