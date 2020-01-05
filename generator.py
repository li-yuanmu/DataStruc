
mygenerator = (i for i in range(3))

a = [i*i for i in range(3)]

def create_generator():
    mylist = range(3)
    for i in mylist:
        yield  i*i
my_generator = create_generator()

print(my_generator)
for i in my_generator:
    print(i)

print(mygenerator)
print(a)

for i in a:
    print(i)

for i in mygenerator:
    print(i)

print()