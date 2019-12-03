# -*- coding: utf-8 -*-
# @Time    : 2019/11/15 13:45
# @Author  : DelayWu
# @Email   : DelayWu@163.com


# 什么是扁平序列和
# 这类 序列只能容纳一种类型。
#
# 容器序列
# 这些序列能存放不同类型的数据

# list comprehension  generator expression genexps
import collections

symbols = '$¢£¥€¤'

codes = []

for symbol in symbols:
    codes.append(ord(symbol))

print(codes)

codes = [ord(symbol) for symbol in symbols]
print(codes)

beyond_ascii = [ord(symbol) for symbol in symbols if ord(symbol) > 127]
print(beyond_ascii)

beyond_ascii = list(filter(lambda o: o > 127, map(ord, symbols)))

print(beyond_ascii)

codes = (ord(symbol) for symbol in symbols)

print(type(codes))

name = ('wuyue', 'mawenwen')

a, b, *c = name

print(a, b, c)

*a, = range(5)

print(a)

a = 1
b = 2

a, b = b, a

print(a, b)

print(divmod(20, 8))

t = (20, 8)

print(*t)

print(divmod(*t))

*head, b, c, d = range(5)

print(head)

print(*head)


class Student:
    def __init__(self):
        self.name = 'wuyue'

    pass


stu = Student()

print(dir(Student))
print(dir(stu))

print(stu.__dict__)
# print(Student.__dict__)

Cart = collections.namedtuple('Cart', ['name', 'age'])

cart = Cart(name='wuyue', age=20)

print(cart._fields)

print(cart._asdict())

cart = Cart._make(('delaywu', 22))

print(cart._asdict())

for key, value in cart._asdict().items():
    print(key, '===', value)
