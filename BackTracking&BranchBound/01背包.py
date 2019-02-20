# 回溯 or 分支限界

bestV = 0               # 最高价值
curW = 0                # 当前物品重量
curV = 0	            # 当前物品价值
bestx = None	        # 最好x
# 回溯函数
def backtrack(i):
	# i:开始位置
	# x:物品
	global bestV, curW, curV, x, bestx
	if i >= n:			# 边界条件
		if bestV < curV:
			bestV = curV
			bestx = x[:]
	else:	            # 更新
		if curW + w[i] <= c:
			x[i] = True
			curW += w[i]
			curV += v[i]
			backtrack(i+1)
			curW -= w[i]
			curV -= v[i]
		x[i] = False
		backtrack(i+1)

if __name__ == '__main__':
	n = 5	           # 物品数量
	c = 10             # 背包最大承受重量
	w = [2,2,6,5,4]	   # 每个物品重量
	v = [6,3,5,4,6]	   # 每个物品价值
	x = [False for i in range(n)]
	backtrack(0)
	print(bestV)
	print(bestx)