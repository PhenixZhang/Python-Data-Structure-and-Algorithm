# Example 1:
# coins = [1, 2, 5], amount = 11
# return 3 (11 = 5 + 5 + 1)
#
# Example 2:
# coins = [2], amount = 3
# return -1.
# 题目描述：给一些面额的硬币，要求用这些硬币来组成给定面额的钱数，
# 并且使得硬币数量最少。硬币可以重复使用。
#
# 物品：硬币
# 物品大小：面额
# 物品价值：数量
# 因为硬币可以重复使用，因此这是一个完全背包问题。

# 拓展 要求最大硬币呢 硬币个数有限制呢

import numpy as np


def coinChange(coins, amount):
    dp = np.array([float("inf")] * (amount+1))
    dp[0] = 0
    def CP(coin,amount,dp):
        for j in range(amount+1):
            dp[j] = min(dp[j-coin]+1, dp[j])

    for i in range(len(coins)):
        CP(coins[i], amount, dp)

    return int(dp[-1]) if dp[-1] <= amount else "no result..."


if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 11

    print(coinChange(coins, amount))

    print("-----------------------------")
