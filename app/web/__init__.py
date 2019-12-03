from collections.abc import Iterable, Iterator

print('ok')

names = [1, 2, 3, 4, 5, 6, 7]

# print(isinstance(iterator,names))

print(isinstance(1, int))

print(isinstance(names, Iterable))
names1=iter(names)


print(isinstance(iter(names),Iterator))

print(next(names1))
print(next(names1))
print(next(names1))

# list dict tuple string set =>iterable



print(isinstance('123',Iterable))

# 通过iter函数可以将iterable可迭代对象转为迭代器

a=[1,2,3,4,5,6]

b=iter(a)

print(isinstance(b,Iterator))

# 生成器

def d():
    print('初始化')
    sum = 0
    value = yield sum
    sum = sum + value
    print('sum的值是：%d' % sum)
    value = yield sum
    sum = sum + value
    print('sum的值是：%d' % sum)
    value = yield sum
    sum = sum + value
    print('sum的值是：%d' % sum)
    return sum+1

c = d()          # c是一个生成器，此行代码并不运行d()内容
a = c.send(None) # 启动生成器，遇到d()的第一个yield时中断
print('生成器传出的值:%d' % a)
a = c.send(1)
print('生成器传出的值:%d' % a)
a = c.send(1)
print('生成器传出的值:%d' % a)