# -*- coding: utf-8 -*-
# @Time    : 2019/11/15 15:23
# @Author  : DelayWu
# @Email   : DelayWu@163.com


# 切片  slice


l = [10, 20, 30, 40, 50, 60]

print(l[:2])

print(l[2:])

s = 'bicycle'

print(s[::3])

l = list(range(10))

print(l)

l[2:5] = [100]

print(l)

l = [1, 2, 3] * 5

print(l)

print(5 * 'abcde')

self_list = [[]] * 3
print(self_list)
print(id(self_list[0]))
print(id(self_list[1]))

