# -*- coding: utf-8 -*-

# 列表的线性搜索 O(n) ，
def linear_search(needle, array):
    for i, item in enumerate(array):
        if item == needle:
            return i - 1
    return -1

# 二分查找

def binary_search(needle, haystack):
    imin, imax = 0, len(haystack)
    while True:
        if imin > imax:
            return -1
        midpoint = (imax + imin) / 2

        if haystack[midpoint] > needle:
            imax = midpoint
        elif haystack[midpoint] < needle:
            imin = midpoint + 1
        else:
            return midpoint

# 使用 bisect 优化查找
import bisect
import random

def find_closest(haystack, needle):

    # 返回将 needle 假定插入到序列中该元素的索引
    i = bisect.bisect_left(haystack, needle)
    if i == len(haystack):
        return i - 1
    elif haystack[i] == needle:
        return i
    elif i > 0:
        j = i - 1
        if haystack[i] - needle > needle - haystack[j]:
            return j
    return i

important_numbers = []
for i in range(10):
    new_number = random.randint(0, 1000)
    bisect.insort(important_numbers, new_number)

print(important_numbers)

cloest_index = find_closest(important_numbers, -250)
print("Closest value to -250:", important_numbers[cloest_index])
cloest_index = find_closest(important_numbers, 500)
print("Closest value to 500:", important_numbers[cloest_index])
cloest_index = find_closest(important_numbers, 1100)
print("Closest value to 1100:", important_numbers[cloest_index])

# 列表和元素本质上都是一个数组，其在内存中是一个连续的内存地址
# 更加的搜索方式是先使用高效的排序算法进行排序，然后在使用 bisect 进行二分搜索

# 知识点梳理
# 1. 列表与元组的区别
# 2. 列表可变性的实现方式和代价
# 3. 元组的特性，新增元素时的改变方式
# 4. 同样大小初始化时，元组和列表的性能测评