# import sys   
# sys.setrecursionlimit(10000) 
def hanoi(n,source,target,helper):
	if n==1:			                # 边界条件
		moveSingleDesk(source,target)
	else:
		hanoi(n-1,source,helper,target) # 将n-1个盘从A移到C
		moveSingleDesk(source,target)	# 将A中最大的一个盘从A移到B/
		hanoi(n-1,helper,target,source)	# 将n-1个盘从C移到B
def moveSingleDesk(source,target):
	disk = source[0].pop()
	print("moving " + str(disk) + " from " + source[1] + " to " + target[1])
	target[0].append(disk)
if __name__ == '__main__':      
	lst = sorted([i for i in range(1,4)],reverse=True)
	A = (lst, "A")
	B = ([], "B")
	C = ([], "C")
	hanoi(len(A[0]),A,B,C)