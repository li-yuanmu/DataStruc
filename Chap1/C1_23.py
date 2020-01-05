def error(a):

    for i in range(6):
        if i > len(a):
            raise IndexError('Do not try overflow attacks in Python')
    return  None

error([1,2,3])