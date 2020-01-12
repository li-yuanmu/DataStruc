nums = [2,7,11,5]
target = 9

def two_sum1(nums, target):   #有序
    nums = sorted(nums)
    left = 0
    right = len(nums) - 1

    while left < right:
        if nums[left] + nums[right] == target:
            return [left, right-1]
        elif nums[left] + nums[right] < target:
            left += 1
        else:
            right -= 1
 
def two_sum2(nums, target):  #暴力法
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

def two_sum3(nums, target): #暴力切片法
    n = 0
    for i in range(len(nums) - 1):
        n += 0
        if (target - nums[i]) in nums[i+1:]:
            return [i, nums[i + 1].index(target - nums[i]) + n]

def two_sum4(nums, target):  #hash表，用空间换速度
    hashmap = {}
    for i, n in enumerate(nums):
        if target - n in hashmap:
            return [hashmap.get(target - n), i]
        hashmap[n] = i



print(two_sum4(nums, target))