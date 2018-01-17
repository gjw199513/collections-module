# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/17 0017 下午 3:28'

from collections import Counter

# counter用于统计，默认从大到小输出
users = ["bobby1", "bobby2", "bobby3", "bobby1", "bobby2", "bobby2"]
user_counter = Counter(users)
user_counter = Counter("abbadgwwssdd")

# 使用update可以同原有字符加在一起统计
user_counter.update("gwdesd")

# 可以加入一个新的counter对象统计
user_counter2 = Counter("bssd")
user_counter.update(user_counter2)

# most_common()解决top n的问题
print(user_counter.most_common(2))

print(user_counter)
