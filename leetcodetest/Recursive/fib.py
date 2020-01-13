

def fib(n):  #写法最简洁，但是存在大量的重复计算，复杂性为 O(1.618^n)
   
    if n == 0 or n == 1:
        return 1
    
    return fib(n - 1) + fib(n - 2)

def new_fib(n):  #递推法，复杂度为O(n)

    a, b = 0, 1
    for i in range(n + 1):
        a, b = b, a + b 
    return a

def gen_lib(n): #使用生成器的方法
    a, b = 0, 1

    while n > 0:
        a, b = b, a+b
        n -= 1
        yield a
for i in gen_lib(6):
    print(i)





print(new_fib(5))
print(fib(5))