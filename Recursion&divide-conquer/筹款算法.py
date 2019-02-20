def collect_contributions(n):#n为需要筹集的款数
	if (n<=100):
		return 100 #需要此人捐出100元
	else:
		#寻找10个朋友
		friends= [1,2,3,4,5,6,7,8,9,10]
		sum = 0
		for i in range(len(friends)):
			# 从这10个朋友中分别募集n/10元
			sum += collect_contributions(n/10)
		return sum #返回从10个朋友募集到的资金
print(collect_contributions(1000))