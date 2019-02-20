# 回溯法求解旅行商问题
import math

n = 4
x = [0, 1, 2, 3]
# 定义图的字典形式
G = {
    '1': {'2': 30, '3': 6, '4': 4},
    '2': {'1': 30, '3': 5, '4': 10},
    '3': {'1': 6, '2': 5, '4': 20},
    '4': {'1': 4, '2': 10, '3': 20}}
# 定义图的数组形式
graph = [
    [0, 30, 6, 4],
    [30, 0, 5, 10],
    [6, 5, 0, 20],
    [4, 10, 20, 0]]
bestway = ''
# bestcost = 1<<32 # 这里只要是一个很大数就行了 无穷其实也可以
bestcost = math.inf  # 好吧 干脆就无穷好了
nowcost = 0  # 全局变量，现在的花费

def TSP(graph, n, s):
    global nowcost, bestcost
    if (s == n):
        if (graph[x[n - 1]][x[0]] != 0 and (nowcost + graph[x[n - 1]][x[0]] < bestcost)):
            print('best way:', x)
            bestcost = nowcost + graph[x[n - 1]][x[0]]
            print('bestcost', bestcost)
    else:
        for i in range(s, n):
            # 如果下一节点不是自身 而且 求得的值小于目前的最佳值
            if (graph[x[i - 1]][x[i]] != 0 and nowcost + graph[x[i - 1]][i] < bestcost):
                x[i], x[s] = x[s], x[i]  # 交换一下
                nowcost += graph[x[s - 1]][x[s]]  # 将花费加入
                TSP(graph, n, s + 1)
                nowcost -= graph[x[s - 1]][x[s]]  # 回溯上去还需要减去
                x[i], x[s] = x[s], x[i]  # 别忘记交换回来
TSP(graph, n, 1)