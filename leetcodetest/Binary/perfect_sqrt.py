def perfect(num):
    if num < 2:
        return True

    left, right = 0, num//2

    while left <= right:
        ans = left + (right - left) // 2
        if ans * ans == num:
            return True
        elif ans * ans < num:
            left = ans + 1
        else:
            right = ans - 1

    return False


print(perfect(8))