def dot_product(a, b):
    n = len(a)
    c = [0]*n
    for i in range(n):
        c[i] = a[i] * b[i]

    return c

a = [1,2,3]
b = [1,2,3]

print(dot_product(a,b))