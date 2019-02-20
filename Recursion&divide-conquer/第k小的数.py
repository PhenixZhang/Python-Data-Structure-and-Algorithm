# 算法2
# 主函数
def select_fct(array, k):
    if len(array) <= 10:	# 边界条件
        array.sort()
        return array[k]
    pivot = get_pivot(array)	# 得到数组的支点数
    array_lt, array_gt, array_eq = patition_array(array,pivot) # 按照支点数划分数组
    if k < len(array_lt):		# 所求数在支点左边
        return select_fct(array_lt, k)
    elif k < len(array_lt) + len(array_eq):	# 所求数为支点数
        return array_eq[0]
    else: 
        normalized_k = k - (len(array_lt) + len(array_eq))
        return select_fct(array_gt, normalized_k)
# 得到数组的支点数
def get_pivot(array):
	subset_size = 5	# 每一组有5个元素
	subsets = []	# 用于记录各组元素

	num_medians = len(array) // subset_size
	if (len(array) % subset_size) > 0:
		num_medians += 1	#不能被5整除

	for i in range(num_medians):	# 划分成若干组,每组5个元素
		beg = i * subset_size
		end = min(len(array),beg + subset_size)
		subset = array[beg:end]
		subsets.append(subset)
	medians = []
	for subset in subsets:
		median = select_fct(subset,len(subset)//2)	# 计算每一组的中间数
		medians.append(median)
	pivot = select_fct(medians,len(subset)//2)	# 中间数的中间数
	return pivot
# 按照支点数划分数组
def patition_array(array,pivot):
	array_lt = [];array_gt = [];array_eq = []
	for item in array:
		if item < pivot:
			array_lt.append(item)
		elif item > pivot:
			array_gt.append(item)
		else:
			array_eq.append(item)
	return array_lt,array_gt,array_eq

import random
if __name__ == '__main__':
	# 产生100个元素的随机数组
	num = 100
	array = [random.randint(1,1000) for i in range(num)]
	random.shuffle(array)
	# 用O(n)的算法得到第k小的数
	k = 7
	kval = select_fct(array,k)
	print(kval)
	# 用直接排序的结果验证算法正确性
	sorted_array = sorted(array)
	print(sorted_array)
	assert sorted_array[k] == kval