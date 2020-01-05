def sum_sqrt(n):
    a = []

    for i in range(n + 1):
        a.append(i*i)
    return sum(a)



print(sum_sqrt(3))