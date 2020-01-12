#不用除法进行两数相除
def divide(dividend, divisor):
    if not isinstance( divisor,(int)):
        raise TypeError('mistake')
    if divisor == 0:
        raise ValueError('分母不能为0')
    left = dividend
    n = 0

    while left >= divisor:
        left = left - divisor
        n += 1

    return n


print(divide(5,2))
