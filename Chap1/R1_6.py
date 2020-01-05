def sum_odd(n):
    a = []
    for i in range(n + 1):
        if i % 2 != 0:
            a.append(i*i)
    return sum(a)

print(sum_odd(5))
