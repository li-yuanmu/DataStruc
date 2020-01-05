#不用乘法，除法，取余
def is_even(k):
    while k > 0:
        k = k - 2
    if k == 0:
        return True
    else:
        return  False


print(is_even(4))

