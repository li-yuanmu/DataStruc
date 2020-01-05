
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def factor(n):
    for k in range(1, n + 1):
        if n%k == 0:
            yield  k
            print(k)
print(fibonacci())
print(factor(100))