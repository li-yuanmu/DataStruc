def error(a):


    try:
        b = a[5]
    except IndexError:
        print('''Don't try buffer overflow attacks in Python!''')



error([1,2,3])