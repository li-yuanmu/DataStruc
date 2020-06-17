def fib(n):
    a = 0
    b = 1
    while a <= n:
        yield a
        future = a + b
        a = b
        b = future


for i in fib(20):
    print(i)
