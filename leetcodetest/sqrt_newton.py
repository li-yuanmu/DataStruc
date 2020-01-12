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

		

	


print(binary(5))
#print(sqrt_newton(4))
#print(math.sqrt(4))