# -*- coding: utf-8 -*-
import time
import line_profiler

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

@profile
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


# 使用 timeit 模块
# python3.6 -m timeit -n 5 -r 5 -s "import demo01" "demo01.calc_pure_python(desired_width=1000, max_iterations=300)"

# 使用 Unix 的系统 time 命令
# /usr/bin/time -p python demo01.py


# 使用 cProfiler 分析函数的执行

# 直接使用 cProfile 进行分析
#  python -m cProfile -s cumulative cp02/demo01.py

# 将分析结果存储到统计文件中
# python -m cProfile -o profile.stats cp02/demo01.py

# 操作统计文件
import pstats

p = pstats.Stats('profile.stats')
p.sort_stats("cumulative")
# 输出累计时间报告
p.print_stats()
# 输出调用者的信息
p.print_callers()
# 输出哪个函数调用了哪个函数
p.print_callees()


# line_profiler 使用
# 在要测试的函数上添加 @profile 装饰器
# 使用 kernprof 执行对应的 py 文件或者函数， 会生成 lprof 文件
# kernprof -l cp02/demo01.py
#  查看 lprof 文件查看函数每行代码的运行时间
# python -m line_profiler demo01.py.lprof

# mem_profiler 使用
# 在要监控的函数上添加 @profile
# python -m memory_profiler cp02/demo01.py
