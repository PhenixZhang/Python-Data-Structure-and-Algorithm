# 算法1
def count_inversions_simple(A):
	inv_count = 0
	inv_list = []
	lenA = len(A)
	for i in range(lenA):		# 索引A中各个元素
		for j in range(i,lenA):	# 得到A中某个元素所有右边的元素
			if A[i] > A[j]:		# 判断是否存在逆序对数
				inv_count += 1
				inv_list.append([A[i],A[j]])
	return inv_count,inv_list
if __name__ == '__main__':
	alist = [2, 4, 1, 3, 5]
	print(count_inversions_simple(alist))

# 算法2
def count_inversions_dc(A):
	lenA = len(A)
	if len(A) <= 1:             # 边界条件
		return 0,A
	middle = lenA//2
	leftA = A[:middle]
	rightA = A[middle:]
	countLA,leftA = count_inversions_dc(leftA)      # 递归分解
	countRA,rightA = count_inversions_dc(rightA)    # 递归分解
	countLRA,mergedA = merge_and_count(leftA,rightA)# 合并并计算逆序数
	return countLA + countRA + countLRA,mergedA
def merge_and_count(A, B):
    i, j, inv_count =0, 0, 0
    alist = []
    lenA = len(A);lenB = len(B)
    while i<lenA and j<lenB:
        if A[i]<B[j]:
            alist.append(A[i])
            i+=1
        else:                        # b[j]与A当前所有左边元素构成逆序
            inv_count += lenA-i
            alist.append(B[j])
            j+=1
    while i<lenA:                    # 处理A中剩余元素
        alist.append(A[i])
        i+=1
    while j<lenB:                    # 处理B中剩余元素
        alist.append(B[j])
        j+=1
    return inv_count, alist
    
if __name__ == '__main__':
    alist = [2, 4, 1, 3, 5]
    print(count_inversions_dc(alist))