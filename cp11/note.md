### 1. 在 ipython 中使用 memory_profiler 测量内存使用情况

```
# 将 memory_profiler 加载进 memory_profiler
In [1]: %load_ext memory_profiler

# 计算 ipython 的内存占用
In [2]: %memit
peak memory: 43.37 MiB, increment: 0.08 MiB

# 创建一个元素全为 0 的长度为 1 亿的列表，内存占用大约为 760MB
In [3]: %memit [8] * int(1e8)
peak memory: 806.41 MiB, increment: 763.00 MiB
```

