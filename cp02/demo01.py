# -*- coding: utf-8 -*-
import time
import line_profiler
# from memory_profiler import profile
from io import StringIO
import matplotlib

x1, x2, y1, y2 = -1.8, 1.8, -1.8, 1.8

c_real, c_imag = -0.62772, -0.42193

def calc_pure_python(desired_width, max_iterations):
    x_step = (float(x2 - x1) / float(desired_width))
    y_step = (float(y1 - y2) / float(desired_width))
    x = []
    y = []

    ycoord = y2
    while ycoord > y1:
        y.append(ycoord)
        ycoord += y_step

    xcoord = x1
    while xcoord < x2:
        x.append(xcoord)
        xcoord += x_step

    zs = []
    cs = []
    for ycoord in y:
        for xcoord in x:
            zs.append(complex(xcoord, ycoord))
            cs.append(complex(c_real, c_imag))


    print("Length of x:", len(x))
    print("total elements:", len(zs))
    start_time = time.time()
    out_put = calculate_z_serial_purepython(max_iterations, zs, cs)
    end_time = time.time()
    secs = end_time - start_time
    print(calculate_z_serial_purepython.__name__ + 'took', secs, "seconds")
    # assert sum(out_put) == 33219980

# @profile
def calculate_z_serial_purepython(maxiter, zs, cs):
    output = [0] * len(zs)
    for i in range(len(zs)):
        n = 0
        z = zs[i]
        c = cs[i]
        while abs(z) < 2 and n < maxiter:
            z = z*z + c
            n += 1
            output[i] = n
    return output

from functools import wraps
def timefn(fn):
    @wraps(fn)
    def measure_time(*args, **kwargs):
        t1 = time.time()
        result = fn(*args, **kwargs)
        t2 = time.time()
        print("@timefn" + fn.__name__ + " took " + str(t2 - t1) + " seconds")
        return result
    return measure_time
if __name__ == "__main__":
    calc_pure_python(desired_width=100, max_iterations=300)


# 1. 手动计算并打印时间
# 通过 time.time()
#
# 2.使用 timeit 模块
# -s 导入要执行的模块，-n 指定循环次数，-r 指定重复次数。两者的作用在于: timeit 会对语句循环执行 n 次，并计算平均值作为一个结果，然后
# 在重复 r 次选出最好的结果。不指定的话墨迹人是 循环 10 次 重复 5 次
# python3.6 -m timeit -n 5 -r 5 -s "import demo01" "demo01.calc_pure_python(desired_width=1000, max_iterations=300)"

# 也可以在 ipython 中使用: %timeit: %timeit l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 如果只是简单的查看某条单独语句的执行时间，使用 %timeit 非常方便

# 3. 使用 Unix 的系统 time 命令
# /usr/bin/time -p python demo01.py
# -p 开关



# 4。使用 cProfiler 分析函数的执行

# 直接使用 cProfile 进行分析
# -s 告诉
#  python -m cProfile -s cumulative cp02/demo01.py

# 将分析结果存储到统计文件中
# python -m cProfile -o profile.stats cp02/demo01.py

# 操作统计文件
# import pstats
#
# p = pstats.Stats('profile.stats')
# p.sort_stats("cumulative")
#  ncalls       tottime  percall    cumtime             percall             filename:lineno(function)
#  函数执行次数   累计耗时  每次耗时     包括子函数的执行时间  每次的执行时间         文件名+代码行数+方法名
# 输出累计时间报告
# p.print_stats()
# 输出调用者的信息
# p.print_callers()
# 输出哪个函数调用了哪个函数
# p.print_callees()


# 5. line_profiler 使用
# 在要测试的函数上添加 @profile 装饰器
# 使用 kernprof 执行对应的 py 文件或者函数， 会生成 lprof 文件
# kernprof -l cp02/demo01.py   -l 表示逐行分析， -v用于输出显示，不带 -v 的话会生成对应的 .lprof 文件，然后可以使用 line_profiler 进行查看
#  查看 lprof 文件查看函数每行代码的运行时间
# python -m line_profiler demo01.py.lprof
# Line #      Hits         Time         Per Hit         % Time      Line Contents
# 代码行数     执行次数      占用的总时间   每次执行的时间    时间占比      代码内容

#
# memory_profiler 使用
# 在要监控的函数上添加 @profile
# python -m memory_profiler cp02/demo01.py
# mprof 可视化操作
# mprof run cp02/demo01.py  生成统计文件
# mprof plot mprofile_20170904220625.dat  展示统计文件
# 需要安装 matplotlib, 执行时可能遇到 RuntimeError: Python is not installed as a framework.
# 解决链接如下
# https://stackoverflow.com/questions/21784641/installation-issue-with-matplotlib-python

# run 的 5 个命令
#  run      run a given command or python file
#     rm       remove a given file generated by mprof
#     clean    clean the current directory from files created by mprof
#     list     display existing profiles, with indices
#     plot     plot memory consumption generated by mprof run



# 其他几种工具
# Guppy 项目中的 heapy 工具，可以查看 Python 堆中对象的数量以及每个对象的大小，但是目前只能在 2.7 中使用
# dowser, 可以在代码运行时钩入名字空间并通过 CherryPy 接口 在一个WEB 服务器上提供一个实时的变量示例图，对于分析长期运行的进程时很有用
# 不过也是只能用于 Python 2
# dis ，使我们看到基于栈的 Cpython 虚拟机中运行的字节码

# dis 是内建的，可以传给它一段代码或者一个模块，它会打印出分解的字节码
# import dis
# dis.dis(calculate_z_serial_purepython)
