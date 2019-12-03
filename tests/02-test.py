# -*- coding: utf-8 -*-
# @Time    : 2019/11/15 13:20
# @Author  : DelayWu
# @Email   : DelayWu@163.com

import os
import random
import time

print(os.cpu_count())

from multiprocessing import Process, pool, Lock, Queue, Pipe

print(random.randrange(1, 5))


def piao(name):
    print('%s piao' % name)
    time.sleep(random.randrange(1, 5))
    print('%s piao end' % name)


p1 = Process(target=piao, args=('a',))

p1.start()
print('主线程')
