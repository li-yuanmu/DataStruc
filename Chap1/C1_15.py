def differ(a):
    b = list(set(a))
    if len(a) == len(b):
        print('互不相同')
    else:
        print('有相同的')

a = [1,2,2,3]
differ(a)


for i in a:
    i *=2
    print(i)