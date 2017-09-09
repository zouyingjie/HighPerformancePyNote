# -*- coding: utf-8 -*-

def range(start, stop, step=1):
    numbers = []
    while start < stop:
        numbers.append(start)
        start += step
    return numbers

# 使用 yield的方式进行值的返回，是在循环中一次次的返回值，而不是一下子返回一个列表，节省了内存
def xrange(start, stop, step=1):
    while start < stop:
        yield start
        start += step

for i in range(1, 10000):
    pass

for i in xrange(1, 10000):
    pass



from random import normalvariate, random
from itertools import count

def read_data(file_name):
    with open(file_name) as fd:
        for line in fd:
            data = line.strip().split(',')
            yield map(int, data)

def read_fake_data(file_name):
    for i in count():
        sigma = random()
        yield (i, normalvariate(0, sigma))