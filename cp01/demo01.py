import math
#
# a = 12
# num = math.sqrt(123)
# print(num)

path = "/Users/zouyingjie/soft/python/HighPerformancePyNote/cp01/note.md"
wpath = "/Users/zouyingjie/soft/python/HighPerformancePyNote/cp01/note2.md"

with open(path, 'r') as f:
    content = f.readline().encode()
    result = content.decode()
    print(content)
    print(result)



import codecs