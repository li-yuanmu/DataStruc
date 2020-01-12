#线性时间
def count_sorting(arr):
	if not isinstance(arr, (list)):
		raise TypeError('error para type')

	temp = [0] * (max(arr)+1)
	res = [0] * len(arr)

	for k in arr:
		temp[k-1] += 1
	for j in range(1, len(temp)):
		temp[j] = temp[j] + temp[j-1]
	for i in range(len(arr)-1, -1, -1):
		res[temp[arr[i]] - 1] = arr[i]
		temp[arr[i]] -= 1
	return res








def count_sort(arr):
	if not isinstance(arr, (list)):
		raise TypeError('error para type')

	maxNum = max(arr)
	minNum = min(arr)
	length = maxNum - minNum + 1

	#构造中间数组
	tempArr = [0 for i in range(length)]

	#创建结果数组
	resArr = list(range(len(arr)))

	#第一次遍历,统计每个数字出现的次数
	for num in arr:
		tempArr[num - minNum] += 1

	#第二次遍历
	for j in range(1, length):
		tempArr[j] = tempArr[j] + tempArr[j-1]

	#第三次遍历
	for i in range(len(arr) - 1, -1, -1):
		resArr[tempArr[arr[i] - minNum] - 1] = arr[i]
		tempArr[arr[i] - minNum] -= 1
	return resArr


print(count_sorting([1,2,5,3,4]))
