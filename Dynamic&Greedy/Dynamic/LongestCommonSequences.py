# 最长公共子序列

# "mannbnciow"
# "xxawebqcp"
# 最长公共子序列为: "abc"


# 对于两个子序列 S1 和 S2，找出它们最长的公共子序列。
#
# 定义一个二维数组 dp 用来存储最长公共子序列的长度，
# 其中 dp[i][j] 表示 S1 的前 i 个字符与 S2 的前 j 个字符最长公共子序列的长度。
# 考虑 S1i 与 S2j 值是否相等，分为两种情况：
#
# 当 S1i==S2j 时，那么就能在 S1 的前 i-1 个字符与 S2 的前 j-1 个字符最长公共子序列的基础上
# 再加上 S1i 这个值，最长公共子序列长度加 1，即 dp[i][j] = dp[i-1][j-1] + 1。
# 当 S1i != S2j 时，此时最长公共子序列为 S1 的前 i-1 个字符和 S2 的前 j 个字符最长公共子序列，
# 或者 S1 的前 i 个字符和 S2 的前 j-1 个字符最长公共子序列，取它们的最大者，
# 即 dp[i][j] = max{ dp[i-1][j], dp[i][j-1] }。
# 综上，最长公共子序列的状态转移方程为：
# dp[i][j] = dp[i-1][j-1] if S1i == S2j
#            max(dp[i-1][j],dp[i][j-1])  if  S1i != S2j

import numpy as np


def lengthOfLCS(str1, str2):
    n1 = len(str1)
    n2 = len(str2)
    dp = np.zeros((n1+1,n2+1),dtype=np.int32)
    # i 表示最远考虑到str1的下标第i-1号字符，j表示最远考虑到str2的下标第j-1号字符
    for i in range(1,n1+1):
        for j in range(1,n2+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[n1][n2]


if __name__ == "__main__":
    str1 = "mannbnciow"
    str2 = "xxawebqcp"
    print(lengthOfLCS(str1, str2))




