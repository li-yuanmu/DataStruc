import copy
'''
a = [[1,2],[3,4]]

b = a

c = copy.copy(a)  #浅拷贝

d = copy.deepcopy(a)  #深拷贝

d[0][0] = 'a'
print(a)
print(c)
print(d)

'''

a = [[1,2],[3,4]]

b = copy.copy(a)

b[1] = ['a','b']

print(a)
print(b)

