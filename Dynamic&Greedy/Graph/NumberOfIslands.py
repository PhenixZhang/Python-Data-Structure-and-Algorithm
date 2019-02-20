# -- coding:utf-8 --

# Input:
# 11000
# 11000
# 00100
# 00011
#
# Output: 3


def numIslands(graph):
    if graph is None or len(graph) == 0:
        return 0

    m = len(graph)
    n = len(graph[0])
    islandsNum = 0
    for i in range(m):
        for j in range(n):
            if graph[i][j] != 0:
                dfs(graph,i,j)
                islandsNum += 1

    return islandsNum


def dfs(graph,r,c):
    m = len(graph)
    n = len(graph[0])
    direction = ((1, 0), (-1, 0), (0, 1), (0, -1))
    if r<0 or r>=m or c<0 or c>=n or graph[r][c]==0:
        return

    graph[r][c] = 0
    for d in direction:
        dfs(graph,r+d[0],c+d[1])



if __name__ == "__main__":
    graph = [[1,1,0,0,0],
             [1,1,0,0,0],
             [0,0,1,0,0],
             [0,0,0,1,1]]

    print(numIslands(graph))




