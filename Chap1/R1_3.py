#不用内置函数min和max来实现
def minmax(data):
    min = data[0]
    max = data[0]
    for i in data:
        if min > i:
            min = i
        if max < i:
            max = i
    return max, min


print(minmax([1,2,3,4]))