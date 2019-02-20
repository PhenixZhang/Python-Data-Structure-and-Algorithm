from timeit import Timer
# 算法2
def max_profit_simple(prices):
	best = 0   #记录当前最优值
	ind_best = [] #记录买进和卖出的时间点
	len_prices = len(prices)
	for i in range(len_prices):
		for j in range(i+1,len_prices):
			if prices[j]-prices[i]>best:
				best = prices[j] - prices[i]
				ind_best = [i,j]
	return ind_best,best

# 算法3
def max_profit_dc(prices):
	len_prices = len(prices)
	if len_prices <= 1: 			# 边界条件
		return 0

	mid = len_prices//2
	prices_left = prices[:mid]
	prices_right = prices[mid:]

	maxProfit_left = max_profit_dc(prices_left)		# 递归求解左边序列
	maxProfit_right = max_profit_dc(prices_right)	# 递归求解右边序列
	maxProfit_left_right = max(prices_right) - min(prices_left)		#跨界情况
	
	return max(maxProfit_left,maxProfit_right,maxProfit_left_right)

# 算法4
def max_profit_lin(prices):
    len_prices = len(prices)
    min_price = 10000
    diff = 0
    for i in range(len_prices):
        if prices[i] < min_price:
            min_price = prices[i]
        diff_new = prices[i] - min_price
        if diff_new > diff:
            diff = diff_new
    return diff

prices = [3,4,5,2,2,4,6,2,6,9,6,10,12,3,10,16,5,3,2]
print(max_profit_simple(prices))
print(max_profit_dc(prices))
print(max_profit_lin(prices))
number = 10000

t1 = Timer("max_profit_simple([3,4,5,2,2,4,6,2,6,9,6,10,12,3,10,16,5,3,2])","from __main__ import max_profit_simple")
print("simple ",t1.timeit(number=number),"milliseconds")
t2 = Timer("max_profit_dc([3,4,5,2,2,4,6,2,6,9,6,10,12,3,10,16,5,3,2])","from __main__ import max_profit_dc")
print("dc ",t2.timeit(number=number),"milliseconds")
t3 = Timer("max_profit_lin([3,4,5,2,2,4,6,2,6,9,6,10,12,3,10,16,5,3,2])","from __main__ import max_profit_lin")
print("lin ",t3.timeit(number=number),"milliseconds")