# Title: Best Time to Buy and Sell Stock
#
# Say you have an array for which the ith element is the price of a given stock on day i.
#
# If you were only permitted to complete at most one transaction
# (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
#
# Example 1:
# Input: [7, 1, 5, 3, 6, 4]
# Output: 5
#
# max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
# Example 2:
# Input: [7, 6, 4, 3, 1]
# Output: 0
#
# In this case, no transaction is done, i.e. max profit = 0.


def stockMaxProfit(prices):
    maxProfit = 0
    minPrice = prices[0]

    for i in range(1,len(prices)):
        if prices[i] > minPrice:
            if prices[i] - minPrice > maxProfit:
                maxProfit = prices[i] - minPrice
        else :
            minPrice = prices[i]

    return maxProfit



# 拓展 不限次数
# 思路
# 贪心 只要盈利，就买卖

def stockMaxProfit2(prices):
    maxProfit = 0
    for i in range(1,len(prices)):
        d = prices[i] - prices[i-1]
        if d > 0:
            maxProfit += d
    return maxProfit



# 拓展 限制最多两次
# 思路
# 先求出第一个最大子数组，避开第一个最大子数组的情况下，再求出第二大子数组，再相加即可

def stockMaxProfit3(prices):
    profit = [0]
    profitRev = [0]
    plen = len(prices)
    minp = prices[0]
    maxp = prices[-1]

    for i in range(1, plen):
        minp, maxp = min(minp, prices[i]), max(maxp, prices[plen - i - 1])
        profit.append(max(profit[i - 1], prices[i] - minp))
        profitRev.append(max(profitRev[i - 1], maxp - prices[plen - i - 1]))

    return max(profit[i] + profitRev[plen - i - 1] for i in range(plen))



if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    print(stockMaxProfit(prices))

    prices1 = [7, 6, 4, 3, 1]
    print(stockMaxProfit(prices1))

    print(stockMaxProfit2(prices))

    print(stockMaxProfit3(prices))






