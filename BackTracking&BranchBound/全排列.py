# 回溯解法
def permute(list,s):
	if list == 1: # 边界条件
		return s
	else:		  # 递归生成
		return [y + x for y in permute(1,s) for x in permute(list - 1,s)]
print(permute(4,['a','b','c','d']))