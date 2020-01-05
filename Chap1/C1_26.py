
def equ():

    temp = input("请输入三个数字")
    nums = list(temp.split(" "))
    a = int(nums[0])
    b = int(nums[1])
    c = int(nums[2])

    if a + b == c or a == b - c or a * b ==c:
        print('成立')
    else:
        print("不成立")

equ()
