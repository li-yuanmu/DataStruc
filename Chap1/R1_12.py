from random import choice
from random import randrange

def my_choice(l):
    """利用randrange实现choice"""
    l = sorted(l)
    a = l[0]
    b = l[-1]
    c = randrange(a,b+1)
    if c in l:
        return c
l = [1,2,5]
print(my_choice(l))
print(choice([1,2,5]))
#print(randrange(1,4))


