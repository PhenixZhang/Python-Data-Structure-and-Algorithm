# -- coding:utf-8 --

# Minimum Path Sum (Medium)
# 题目描述：求从矩阵的左上角到右下角的最小路径和，每次只能向右和向下移动。
# [[1,3,1],
#  [1,5,1],
#  [4,2,1]]
# Given the above grid map, return 7. Because the path 1→3→1→1→1 minimizes the sum.


def minPathSum(graph):
    if len(graph) == 0 or len(graph[0]) == 0:
        return 0
    m = len(graph)
    n = len(graph[0])

    dp = [0] * n
    for i in range(m):
        for j in range(n):
            if j == 0:
                dp[j] = dp[j]
            elif i == 0:
                dp[j] = dp[j-1]
            else :
                dp[j] = min(dp[j-1],dp[j])
            dp[j] += graph[i][j]
    return dp[n-1]


if __name__ == "__main__":
    graph = [[1,3,1],
             [1,5,1],
             [4,2,1]]
    print(minPathSum(graph))