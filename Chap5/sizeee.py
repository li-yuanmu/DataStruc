import sys
"""
创建低层次数组需要明确声明数组的大小
空列表也会请求一定量的内存
"""
n = 27
data = []
for k in range(n):
    a = len(data)
    b = sys.getsizeof(data)
    print('Length:{0:3d}; size in bytes:{1:4d}'.format(a, b))
    data.append(None)