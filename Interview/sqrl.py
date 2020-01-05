#利用牛顿法求平方根
import math

def NewtonSqrl(x):
    y = 4
    while abs(y * y - x) > 1e-6:
        y = (y + x/y) / 2
    return  y

def binarysearch(num):
    y = num / 2
    low = 0
    up = num
    count = 1
    while abs(y**2 - num) > 0.001:
        count += 1
        if y**2 > num:
            up = y
            y = low + (up - low)/2
        elif y**2 < num:
            low = y
            y = up -(up - low)/2


        print(count)
        return y
    if y**2 -num == 0:
        return y

print(NewtonSqrl(4))
print(binarysearch(4))