# 算法1
import math
def  closestpair_simple(X,n):
	min_d = distance(X[0],X[1])		# 记录当前最小距离
	for i,(x,y) in enumerate(X):
		for j in range(i+1,n):
			if distance(X[i],X[j]) < min_d:
				min_p = [X[i],X[j]]	# 记录哪两个点
				min_d = distance(X[i],X[j])
	return min_p,min_d
def distance(a,b):					# 计算两点之间的欧拉距离
	return math.sqrt(math.pow(a[0]-b[0],2)+math.pow(a[1]-b[1],2))
if __name__ == '__main__':
    points = [(2,3), (10, 1), (3, 25), (23,15),
             (18,3), (8,9), (12,30), (25,30),
             (9,2), (13,10), (3,4), (5,6),
             (22,32), (5,32), (23,9), (19,25),
             (14,1), (11,25), (26,26), (12,9),
             (18,9), (27,13), (32,13)]
    print(closestpair_simple(points, len(points)))


# 算法2
import math
# 主函数入口
def closest(P,n):
	X = list(P)
	Y = list(P)
	X.sort() 		# 预处理,按照X轴进行排序
	Y = sort_y(Y)	# 预处理,按照Y轴进行排序
	return closest_pair(X,Y,n)
# 递归求解函数
def closest_pair(X,Y,n):
	if n<= 3:		# 边界条件
		return brute_force(X,n)
	mid = n//2
	Y_Left = []
	Y_Right = []
	for p in Y:
		if p in X[:mid]:
			Y_Left.append(p)	#  Y_left中为直线L左边的所有点且其Y轴坐标值依次增大
		else:
			Y_Right.append(p)	# Y_right中为直线L左边的所有点且其Y轴坐标值依次增大
	dis_left = closest_pair(X[:mid],Y_Left,mid) # 递归处理PL
	dis_right = closest_pair(X[mid:],Y_Right,n-mid) #递归处理PR
	min_dis = min(dis_left,dis_right)   # 得到PL和PR中的最小距离
	strip = []
	for (x,y) in Y:
		if abs(x - X[mid][0]) < min_dis:    # 只有L+/-min_dis之间的点才考虑
			strip.append((x,y))
	return min(min_dis,strip_closest(strip,min_dis))
# 边界求解函数
def strip_closest(strip,d):
	min_d = d
	for i,(x,y) in enumerate(strip):
		for j in range(i+1,8):  # 只需要考虑最多7个点
			if i+j < len(strip):# 预防数组越界
				temdis = distance(strip[i],strip[j])
				if temdis < min_d:
					min_d = temdis
		return min_d
# 计算两点间的欧拉距离
def distance(a,b):
	return math.sqrt(math.pow(a[0]-b[0],2) + math.pow(a[1]-b[1],2))
# 按照y轴坐标进行排序
def sort_y(tuples):
	return sorted(tuples,key = lambda last:last[-1])
# 当点数小于3时，直接计算最小距离
def brute_force(X,n):
	min_d = distance(X[0],X[1])
	for i,(x,y) in enumerate(X):
		for j in range(i+1,n):
			if distance(X[i],X[j]) < min_d:
				min_d = distance(X[i],X[j])
	return min_d
if __name__ == '__main__':
    print (closest(points, len(points)))