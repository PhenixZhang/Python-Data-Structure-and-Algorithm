def permutation(str):
	lenstr = len(str)
	if lenstr < 2:#边界条件
		return str
	else:
		result = []
		for i in range(lenstr):
			ch = str[i]   #取出str中每一个字符
			rest = str[0:i] + str[i+1:lenstr]
			for s in permutation(rest): #递归
				result.append(ch + s) #将ch与子问题的解依次组合
	return result
print(permutation('daswg'))