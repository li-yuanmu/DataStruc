import math

def sqrt_newton(a):

	x = a

	while abs(x*x - a) > 0.0001:
		x = (x + a/x) / 2
	return x
	
def binary(a):   

	l = 0

	r = a

	mid = (l + r) / 2.0
	
	while abs(mid**2 - a) > 0.1:
		if mid**2 > a:
			r = mid
		else:
			l = mid
		mid = (l + r) / 2.0
	print(mid)

def binary_sqrt(x):
	left = 0
    right = x // 2 + 1

     while left < right:
        mid = (right + left + 1) // 2
        square = mid*mid
        if square > x:
            right = mid - 1
        else:
            left = mid + 1
    return left   
        

		

	


print(binary(5))
#print(sqrt_newton(4))
#print(math.sqrt(4))