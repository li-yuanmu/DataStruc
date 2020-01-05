
def num(str):
    temp = {'a', 'e', 'i','o','u'}
    count = 0
    for i in str:
        if i in temp:
            count += 1
    print(count)

num("abcu")