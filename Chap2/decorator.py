#装饰器
def check(func):
    def inside(a, b):
        if b == 0:
            print('不能除0')
            return 
        func(a, b)
    return inside

@check
def div(a, b):
    return a / b

#div = check(div)

print(div(4, 0))