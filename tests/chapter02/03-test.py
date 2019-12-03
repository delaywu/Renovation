# -*- coding: utf-8 -*-
# @Time    : 2019/11/15 15:46
# @Author  : DelayWu
# @Email   : DelayWu@163.com
import random

a=[1,2,3]
b=[4,5,6]

a.extend(b)
print(id(a))
a=a+b

print(id(a))
print(a)

t = (1, 2, [30, 40])

t[2].extend([50,60])

print(t)

a=[1,2,3,4,5]

random.shuffle(a)

print(a)