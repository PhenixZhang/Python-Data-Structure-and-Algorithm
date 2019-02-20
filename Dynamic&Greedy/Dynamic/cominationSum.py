# nums = [1, 2, 3]
# target = 4
#
# 同样对硬币的使用没有个数限制  且不考虑顺序
#
# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 3)
# (2, 2)


# 拓展 如果对硬币的使用有个数限制  如类似0-1背包


import numpy as np


# 对个数没有限制的情况 类似于完全背包
def combinationSum(coins, target):
    dp = np.zeros((target+1),dtype=np.int32)
    dp[0] = 1

    def CP(coin, target, dp):
        for j in range(target+1):
            if j >= coin:
                dp[j] += dp[j-coin]

    for i in range(len(coins)):
        CP(coins[i], target, dp)
    return dp[-1]



# 有个数限制0-1
def combinationSum2(coins, target):
    dp = np.zeros((target+1),dtype=np.int32)
    dp[0] = 1

    def ZOP(coin, target, dp):
        for j in range(target,-1,-1):
            if j >= coin:
                dp[j] += dp[j-coin]

    for i in range(len(coins)):
        ZOP(coins[i], target, dp)
    return dp[-1]



if __name__ == "__main__":

    coins = [1, 2, 3]
    target = 4

    print(combinationSum(coins, target))

    print("-----------------------------")
    coins = [1, 2, 3, 4]
    target = 5

    print(combinationSum2(coins, target))


