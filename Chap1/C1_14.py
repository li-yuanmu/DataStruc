def mul_odd(a):
    """是否存在一对乘积是奇数的互不相同的数"""
    a = list(set(a))
    for i in range(len(a)):
        for j in range(i, len(a)):
            if (i*j) % 2 != 0:
                return True
            else:
                return False


a = [1,2,2,3]
print(mul_odd(a))